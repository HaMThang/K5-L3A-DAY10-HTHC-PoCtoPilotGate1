# Phân công Lab 10 · 4 người · từ phút 0 tới lúc lên demo (phút 200)

Đi kèm [CHECKLIST-DAY10.md](CHECKLIST-DAY10.md) (hướng dẫn chi tiết từng câu). File này chỉ trả lời: **ai làm gì, lúc nào, giao cho ai**.

## Chia vai

Đề cho phép Kỹ sư cổng 1–2 người, Sản phẩm 1–2 người, Vận hành 1 người. Với 4 người, chia như sau vì phần kỹ thuật nặng nhất:

| Người | Vai | Giữ file | Câu phụ trách |
|---|---|---|---|
| **A** | Kỹ sư cổng 1 · **giữ máy chính** · gợi ý làm trưởng nhóm | `lab10/guards.py` | 2.1, 2.6, chốt vòng 1, 3.0, 3.5 (code), mọi lần chạy `eval`/`grade` |
| **B** | Kỹ sư cổng 2 · trace, test, monitor | `lab10/monitors.py` | 1.3, 2.2, 2.7, 2.8, 3.1 (trace + C2), 3.6 (C8) |
| **C** | Sản phẩm và kinh doanh | `config/acceptance_criteria.json`, `operating_gates.json` mục `business` | 1.1, 1.6, 2.3, 2.9, B8 (v1), 3.2, C12 (v2) |
| **D** | Vận hành và pháp lý | `operating_gates.json` mục `operations` + `legal`, `submission/submission.json` | 1.2, 1.4, 2.4 (B4, B5), 2.10 (B7.5, B7.6), C3, C4, 3.3, 3.7 (C9–C11) |

Cả bàn: 1.5, pre-mortem 2.5, fault tree C6, chốt quyết định v1 và v2.

## Ba luật làm việc chung (đọc trước khi bắt đầu)

1. **Mọi lệnh `eval`, `gate`, `grade`, `checkpoint`, `criteria sign`, `check_submission` chỉ chạy trên máy của A.** Thư mục `runs/` bị `.gitignore`, lệnh 7 chỉ gom `runs/` trên máy chạy nó. Ai chạy `eval` trên máy mình thì mã lần chạy đó **không có trong bài nộp**, ghi vào phiếu là thành bằng chứng ma. Lệnh `trace` thì ai cũng chạy được trên máy mình.
2. **Mỗi người chỉ sửa mục của mình** trong ba phiếu và file mình giữ (bảng trên). Trước khi sửa: `git pull`. Sửa xong một mục: commit và push ngay. Hai người sửa cùng một đoạn là sinh conflict.
3. **Không ai đụng `config/acceptance_criteria.json` sau khi C ký**, kể cả mở ra xem bằng editor có auto-format. Muốn xem thì dùng `git show HEAD:config/acceptance_criteria.json`.

## Điểm hẹn (cả bàn dừng tay, gặp nhau)

| Phút | Việc | Ai cầm trịch |
|---|---|---|
| 12 | Chốt chia vai, test `OK` trên mọi máy | A |
| 55 | Duyệt Bản tiêu chí trước khi ký | C |
| 75 | Pre-mortem bốn lăng kính (10 phút) | C dẫn, D ghi |
| 100 | Xem report `base · after`, quyết có chốt vòng 1 chưa | A |
| 108 | Chốt quyết định v1 | C |
| 150 | Fault tree trước khi sửa (C6) | B dẫn, D ghi |
| 185 | Chốt quyết định v2 | C |
| 195 | Tập demo 5 phút | A |

---

## Người A · Kỹ sư cổng 1 · máy chính

**Phút 0–15**
- [ ] Tạo repo bằng **Use this template**, đặt tên `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`, chọn Private, mời team chấm quyền Read và mời B, C, D làm collaborator.
- [ ] Clone, gắn `upstream`, đặt `git config user.name/user.email` (mã học viên, email giả).
- [ ] Chạy test ra `OK`, gửi link repo cho cả bàn.

**Phút 15–65** (chưa được chạy `eval`)
- [ ] Đọc `lab10/guards.py`, `lab10/helpers.py`, Phụ lục C của guide. Phác sẵn trên giấy 3–4 ý cổng có thể viết, chờ pre-mortem chọn.
- [ ] Cùng B làm 1.3, cùng bàn làm 1.5.
- [ ] Phút 60–65: khi C báo xong, **chạy lệnh ký trên máy A** rồi commit và push ngay. Báo mã commit cho C để điền A5.

**Phút 65–85**
- [ ] Câu 2.1: chạy `eval` mốc base và `gate`. Gửi **mã lần chạy** và ảnh/đoạn output cho cả bàn (C cần khối kinh doanh, D cần khối hàng chờ).
- [ ] Điền B0 dòng 1 và B1 (lý lẽ tự chặn hay người duyệt, khoanh khuyến nghị).
- [ ] Phút 75: dự pre-mortem.

**Phút 85–105**
- [ ] Câu 2.6: viết 2–3 cổng trong `guards.py` theo lý do pre-mortem đã chọn. Điền B7.1.
- [ ] Mỗi lần sửa: chạy `eval --suite base --stage after --note "..."` và unittest. Ghi vào B0.
- [ ] Nhận config từ C (mục `business`) và D (mục `operations`, `legal`) qua git, chạy lại để xem có ca mới hỏng không.

**Phút 105–115**
- [ ] Chạy `checkpoint`, `eval --stage prepared`, `gate`. Gửi mã prepared cho C.
- [ ] Sau khi C điền B8: commit và push.

**Phút 125–155**
- [ ] Kéo thẻ bằng lệnh `git pull … upstream main` khi Lab Coach báo. Người bốc số có thể là bất kỳ ai.
- [ ] Ghi `Thẻ đã bốc:` ở đầu Phiếu C, chạy `grade --incident Sx` **trước khi sửa gì**. Điền C0 và C1 cùng cả bàn.
- [ ] Đọc `incidents/Sx/card.md` với B, khoanh nguyên nhân nào thuộc code, nguyên nhân nào thuộc config.

**Phút 155–185**
- [ ] Sửa `guards.py` cho phần nguyên nhân kỹ thuật, giữ cổng vòng 1.
- [ ] Chạy `eval --suite Sx --stage after`, `eval --suite base --stage after`, `grade --incident Sx`. Mỗi lần đổi một thứ, ghi `--note`.
- [ ] Gom các thay đổi config của C, D và monitor của B, chạy lại `grade` tới khi có `integrity ✅`, `visible ✅`, `regression ✅`, `monitor ✅`.
- [ ] Điền dòng code trong C7.

**Phút 185–200**
- [ ] Sau khi D điền `submission.json`, chạy `check_submission --collect` tới khi `ĐỦ THÀNH PHẦN`. Push.
- [ ] Mở sẵn report ba cột `base · prepared · after` trên màn hình để demo.

---

## Người B · Kỹ sư cổng 2 · trace, test, monitor

**Phút 0–15**
- [ ] Clone repo của bàn, chạy test ra `OK`. Đọc `lab10/monitors.py` và guide mục Lệnh 3.

**Phút 15–65**
- [ ] Câu 1.3 (A2 cột Offline): chọn một bước của agent, điền Thước đo · Dữ liệu · Cách tính. Bàn với A.
- [ ] Đọc `data/tickets.jsonl` để nắm các kiểu ticket (chỉ đọc, chưa chạy trợ lý).

**Phút 65–85**
- [ ] Câu 2.2: `python -m lab10.trace --suite base --ticket T-002 --seed 55`. Điền B2 đủ ba phần.
- [ ] Phút 75: dự pre-mortem, đóng góp lăng kính kỹ thuật.

**Phút 85–105**
- [ ] Câu 2.8: viết tính chất + 2 ticket `--adhoc`, chạy trên máy mình với `--stage after` sau khi kéo `guards.py` mới nhất của A. Dán kết quả vào B7.3. **Lưu lại 2 ticket này cho demo.**
- [ ] Câu 2.7: viết B7.2 (hai bước tránh rò rỉ dữ liệu).
- [ ] Dò trace các ca A báo hỏng, chỉ ra cổng chặn nhầm ở đâu.

**Phút 125–155**
- [ ] Đọc thẻ cùng A. Dò ít nhất 2 ticket hỏng theo hai kiểu khác nhau: `python -m lab10.trace --suite Sx --ticket <ID> --seed 11`.
- [ ] Điền C2 (≥ 2 lỗi khác nguồn, ≥ 1 lỗi chìm, tác hại cho ai, bao nhiêu).
- [ ] Phút 150: dẫn phần fault tree C6, mỗi lá phải có `ticket@seed` hoặc dòng report.

**Phút 155–185**
- [ ] Câu 3.6: viết **một hàm monitor mới** trong `monitors.py`, đăng ký vào `MONITORS`. Nó phải cho số khác nhau giữa bộ nền và gói sự cố. Push, báo A chạy `grade` kiểm `monitor ✅`.
- [ ] Điền C8 (ba ô).
- [ ] Nếu còn thời gian: tìm lỗi chìm ngoài thẻ mà monitor bắt được (bonus +5), ghi `ticket@seed` vào Phiếu C.

**Phút 185–200**
- [ ] Chuẩn bị phần phản biện: 2 ticket hiểm sẵn lệnh để chạy ngay, và một câu hỏi soi cho bàn cặp.

---

## Người C · Sản phẩm và kinh doanh

**Phút 0–15**
- [ ] Clone, chạy test. Mở `data/world.json`, đọc `ops_limits`, `ops_facts`, `policies`, `warehouses`.

**Phút 15–65** (việc nặng nhất của C)
- [ ] Câu 1.1 (A1).
- [ ] Câu 1.6 (A4): câu "Nếu … thì chúng tôi sẽ …", bốn câu soát, hai câu ranh giới đầu ra.
- [ ] Điền `config/acceptance_criteria.json`: `team` **giống hệt** tên repo, mọi ngưỡng, `stop_condition`, bốn `decision_rule`. Mỗi ngưỡng phải có một câu lý do bàn nói được lúc demo.
- [ ] Phút 55: đưa cả bàn duyệt. Phút 60: push file, báo A ký. Điền A5 khi A gửi mã commit.

**Phút 65–85**
- [ ] Câu 2.3 (B3): bản đồ dữ liệu và một ví dụ drift cụ thể.
- [ ] Đọc khối "kinh doanh và vận hành" từ output của A: chi phí mỗi ticket, ROI, tổng tiền hoàn.
- [ ] Phút 75: dẫn pre-mortem, giữ lăng kính kinh doanh.

**Phút 85–105**
- [ ] Câu 2.9: điền mục `business` trong `operating_gates.json`, mỗi số một câu lý do từ `ops_limits`/`ops_facts`. Điền B7.4. Push, báo A chạy lại.

**Phút 105–115**
- [ ] Với mã prepared của A, điền cột v1 ở B8: quyết định, ba bằng chứng có mã lần chạy, dòng `decision_rule`, kho/hãng xấu nhất, ngày quyết định lại. Phút 108 chốt với bàn.

**Phút 125–185**
- [ ] Câu 3.2 (C5): một specification kiểm được bằng code hoặc số trong report.
- [ ] Đọc bảng kinh doanh ba mốc trong report `grade`. Nếu nguyên nhân là chi phí hoặc phạm vi: chỉnh `business.pilot_scope`, trần tiền. Ghi dòng của mình vào C7.
- [ ] Theo dõi dòng cuối report: còn vượt trần không, có "được phép cân nhắc Tiếp tục" không.

**Phút 185–200**
- [ ] Điền C12: quyết định v2, đổi hay giữ so với v1 vì con số nào, mã ba mốc, **ba dòng bắt buộc có số**. Phút 185 chốt với bàn.
- [ ] Gửi ba dòng cho D chép vào `submission.json`.
- [ ] Chuẩn bị nói phần "quyết định v2 và con số nào đỡ cho nó" lúc demo.

---

## Người D · Vận hành và pháp lý

**Phút 0–15**
- [ ] Clone, chạy test. Điền bảng thành viên trong `TEAM.md` (họ tên, MSSV, vai của cả 4 người). Push.

**Phút 15–65**
- [ ] Câu 1.2 (A1): mục tiêu từ chị Oanh (`NV-OANH`) và chị Hạnh (`NV-HANH`).
- [ ] Câu 1.4 (A2 cột Telemetry): thước đo không cần nhãn, có khung thời gian và ngưỡng báo động.
- [ ] Đọc guide mục "Cổng trong config" và Phụ lục D (hàng chờ) để chuẩn bị cho 2.10.

**Phút 65–85**
- [ ] Câu 2.4: B4 HAZOP vòng 1 (≥ 3 dòng trên một tool ghi + ≥ 2 dòng ngoài kỹ thuật).
- [ ] B5 checklist 9 nhóm việc, mỗi dòng có PIC có tên.
- [ ] Phút 75: ghi biên bản pre-mortem vào B6, giữ lăng kính con người và pháp lý.

**Phút 85–105**
- [ ] Câu 2.10: điền mục `operations` và `legal` trong `operating_gates.json`. Push, báo A chạy lại.
- [ ] B7.5 runbook 1–3 **khớp đúng các số vừa điền**, có thời hạn dừng và người bấm.
- [ ] B7.6 giờ cao điểm.

**Phút 125–155**
- [ ] C3: phần riêng theo thẻ (bỏ qua nếu bốc S4).
- [ ] C4: HAZOP của thẻ, mục riêng, ≥ 3 dòng.
- [ ] Câu 3.3 (C5): một giả định môi trường dễ sai.
- [ ] Phút 150: ghi fault tree C6.

**Phút 155–185**
- [ ] Nếu nguyên nhân thuộc người hoặc quy trình: chỉnh `reviewers_on_shift`, `review_sampling_pct`, `decision_note`, `legal.*`. Nhớ mỗi người trực tốn 30.000đ/ca, đừng thêm người vô tội vạ. Ghi dòng của mình vào C7.
- [ ] C9 fault tree sau khi sửa, C10 risk register, C11 checklist + runbook 4–5.

**Phút 185–200**
- [ ] Điền `submission/submission.json`: `team` giống tiêu chí, `members` dạng `"HoVaTen-MSSV"` khớp `TEAM.md`, `incident`, `decision_v1`, `decision_v2`, `three_lines` từ C. Push, báo A chạy lệnh 7.
- [ ] Nhắc cả bàn viết mục cá nhân trong `TEAM.md` (có thể viết sau demo, trước deadline).

---

## Kịch bản demo 5 phút (tập ở phút 195)

| Phút | Ai nói | Nội dung |
|---|---|---|
| 0:00–1:00 | A | Chiếu report ba cột `base · prepared · after`. Cổng vòng 1 đỡ được gì trước khi biết thẻ. |
| 1:00–2:30 | B | Sự cố hỏng thế nào (2 ticket, fault tree), monitor mới bắt được gì. |
| 2:30–3:30 | D | Phần sửa là code, con số hay người, vì sao đúng chỗ đó. Cổng nào bàn không nghĩ tới và thuộc lăng kính nào. |
| 3:30–5:00 | C | Quyết định v2, con số nào đỡ cho nó, ba dòng bắt buộc. |

Khi bàn cặp phản biện: A chạy lệnh trên máy chính, người phụ trách phần bị hỏi trả lời. **Sau demo, trả mọi con số đổi thử về bản v2**, A chạy lại `grade` và lệnh 7 rồi push lần cuối.
