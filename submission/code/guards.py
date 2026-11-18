"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


# Trường tối thiểu được gửi hãng khi policy không khai carrier_notice_fields (không có tên, SĐT, địa chỉ, lời khách).
SAFE_NOTICE_FIELDS = {"order_id", "parcel_id", "district", "delay_days"}


def _facts(ctx, order_id):
    """Sự thật từ DB cho một đơn: (order, parcel của ticket, độ trễ theo tracking, policy hiệu lực theo ngày)."""
    order = ctx.tools.lookup_order(order_id)
    if order is None:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    return order, parcel, H.db_delay_days(parcel, ctx.as_of), policy


def _valid_approval(ctx, approval_id, order_id, amount):
    """Phê duyệt chỉ hợp lệ khi đúng đơn, còn hiệu lực, chưa dùng và đủ hạn mức."""
    if not approval_id:
        return False
    for a in ctx.tools.lookup_approvals(approval_id=approval_id):
        if (a.get("status") == "valid" and a.get("order_id") == order_id
                and H.d(a["expires_at"]) >= H.d(ctx.as_of) and amount <= a.get("max_vnd", 0)):
            return True
    return False


def _auto_refund_today_for(ctx, customer_id):
    """Tổng đã hoàn tự động (không phê duyệt) hôm nay cho một khách; bỏ các dòng sổ cái của những ngày trước."""
    # shortcut: đọc thẳng world vì ReadTools chỉ có tổng cả ngày; đổi khi tools có bản lọc theo khách.
    w = ctx.tools._w
    return sum(r["amount_vnd"] for r in w.ledger[w.seed_rows:]
               if r.get("customer_id") == customer_id and not r.get("approval_id"))


def pre_guard(ctx):
    # Cổng 0: ghim policy theo ngày hiệu lực, không tin cờ index_active (cờ có thể cũ khi policy đổi version).
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không có chính sách hiệu lực cho ngày hôm nay")
    return Verdict.allow(policy_id=policy["policy_id"])


def _refund_gate(ctx, action):
    # Cổng 1a: mỗi đơn chỉ hoàn một lần (agent ghi lại khi LLM confirm lỗi; cờ refund_status chỉ cập nhật ban đêm).
    if ctx.tools.ledger_rows(order_id=action["order_id"]):
        return Verdict.deny("đơn đã có dòng hoàn trong sổ cái")
    facts = _facts(ctx, action["order_id"])
    if not facts or not facts[3]:
        return Verdict.escalate("không xác minh được đơn hoặc chính sách, chuyển người duyệt")
    order, parcel, delay, policy = facts

    # Cổng 1b: số tiền tính lại từ tracking DB + policy hiệu lực, không theo số ngày khách khai, lệnh trong ticket
    # hay nhánh fail_open khi LLM lỗi.
    entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    if entitled <= 0:
        return Verdict.deny(f"theo tracking DB trễ {delay} ngày, nguyên nhân {parcel.get('delay_cause')}: "
                            "không đủ điều kiện hoàn")
    changes = {}
    amount = action.get("amount_vnd", 0)
    if amount > entitled or action.get("basis") == "fail_open":
        amount = changes["amount_vnd"] = entitled

    # Cổng 1c: không trừ tiền shop; quyền lợi trễ hạn do LogiX trả.
    if action.get("payer", "LOGIX") != "LOGIX":
        changes["payer"] = "LOGIX"

    # Cổng 1d: vượt hạn mức tự động thì phải có phê duyệt hợp lệ cho đúng đơn này.
    approved = _valid_approval(ctx, action.get("approval_id"), order["order_id"], amount)
    if amount > policy["auto_limit_vnd"] and not approved:
        return Verdict.escalate(f"{amount}đ vượt hạn mức tự động {policy['auto_limit_vnd']}đ, "
                                "chưa có phê duyệt hợp lệ cho đơn này")
    if action.get("approval_id") and not approved:
        changes["approval_id"] = None

    # Cổng 1e: trần đã thống nhất với Ops/Finance, kiểm TRƯỚC khi tiền vào sổ.
    limits = ctx.tools.ops_limits()
    cap = limits.get("max_auto_refund_per_customer_per_day_vnd")
    if not approved and cap is not None and _auto_refund_today_for(ctx, order["customer_id"]) + amount > cap:
        return Verdict.escalate(f"tổng hoàn tự động cho khách {order['customer_id']} hôm nay vượt {cap}đ")
    strikes = limits.get("max_auto_strikes_per_carrier_per_day")
    if (strikes is not None and H.carrier_at_fault(policy, parcel, delay)
            and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= strikes):
        return Verdict.escalate(f"hãng {parcel['carrier_id']} đã bị ghi {strikes} lỗi tự động hôm nay")

    if changes:
        return Verdict.modify(f"theo DB: trễ {delay} ngày, quyền lợi {entitled}đ, policy {policy['policy_id']}",
                              **changes)
    return Verdict.allow()


def _fault_gate(ctx, action):
    # Cổng 2: chỉ ghi lỗi cho đúng kiện, đúng hãng, khi tracking ghi nguyên nhân thuộc lỗi hãng (bảo vệ bên thứ ba).
    facts = _facts(ctx, action["order_id"])
    if not facts or not facts[3]:
        return Verdict.deny("không xác minh được đơn hoặc chính sách, không ghi lỗi hãng")
    order, parcel, delay, policy = facts
    if not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny(f"tracking không cho thấy lỗi hãng (trễ {delay} ngày, "
                            f"nguyên nhân {parcel.get('delay_cause')})")
    if (action.get("parcel_id"), action.get("carrier_id"), action.get("delay_days")) !=             (parcel["parcel_id"], parcel["carrier_id"], delay):
        return Verdict.modify("ghi lỗi theo kiện trễ và độ trễ trong tracking DB",
                              parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                              driver_id=parcel.get("driver_id"), delay_days=delay)
    return Verdict.allow()


def _notify_gate(ctx, action):
    # Cổng 3: hãng chỉ nhận các trường policy cho phép, bỏ lời khách và thông tin người nhận.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    allowed = set((policy or {}).get("carrier_notice_fields") or SAFE_NOTICE_FIELDS)
    payload = action.get("payload") or {}
    if set(payload) - allowed:
        return Verdict.modify("bỏ trường ngoài carrier_notice_fields trước khi gửi hãng",
                              payload={k: v for k, v in payload.items() if k in allowed})
    return Verdict.allow()


def _reply_gate(ctx, action):
    # Cổng 4: số tiền báo khách phải bằng số tiền thật trong sổ cái của ticket.
    paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(ticket_id=action["ticket_id"]))
    if action.get("amount_vnd", 0) != paid:
        return Verdict.modify(f"số tiền báo khách theo sổ cái ({paid}đ)", amount_vnd=paid)
    return Verdict.allow()


GATES = {"issue_refund": _refund_gate, "file_carrier_fault": _fault_gate,
         "notify_carrier": _notify_gate, "send_reply": _reply_gate}


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    gate = GATES.get(action.get("tool"))
    return gate(ctx, action) if gate else Verdict.allow()
