# Tự kiểm tra sự cố S8 · FAIL

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S8-grade-20261118-172627-0d3d70` · bàn: `K5-L3A-DAY10-HTHC-PoCtoPilotGate1` · grader `lab10-1.0` · 1.324s
- Ba mốc: base `R-S8-before-20261118-172628-0d3d70` · prepared `R-S8-prepared-20261118-172628-0d3d70` · after `R-S8-after-20261118-172628-0d3d70` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `88b68b35`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `0d3d70d63016`
- Hash Bản tiêu chí chấp nhận: `2a7352f455fa` · đã ký: `2a7352f455fa` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S8` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S8 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ❌ | file khoá bị đổi: ['data/tickets.jsonl', 'data/world.json', 'incidents/S1/card.json', 'incidents/S1/card.md', 'incidents/S1/tickets.jsonl', 'incidents/S1/world_patch.json', 'incidents/S2/card.json', 'incidents/S2/card.md', 'incidents/S2/tickets.jsonl', 'incidents/S2/world_patch.json', 'incidents/S3/card.json', 'incidents/S3/card.md', 'incidents/S3/tickets.jsonl', 'incidents/S3/world_patch.json', 'incidents/S4/card.json', 'incidents/S4/card.md', 'incidents/S4/tickets.jsonl', 'incidents/S4/world_patch.json', 'incidents/S5/card.json', 'incidents/S5/card.md', 'incidents/S5/tickets.jsonl', 'incidents/S5/world_patch.json', 'incidents/S6/card.json', 'incidents/S6/card.md', 'incidents/S6/tickets.jsonl', 'incidents/S6/world_patch.json', 'incidents/S7/card.json', 'incidents/S7/card.md', 'incidents/S7/tickets.jsonl', 'incidents/S7/world_patch.json', 'incidents/S8/card.json', 'incidents/S8/card.md', 'incidents/S8/tickets.jsonl', 'incidents/S8/world_patch.json', 'lab10/__init__.py', 'lab10/_gradectx.py', 'lab10/_noop_guards.py', 'lab10/agent.py', 'lab10/check_submission.py', 'lab10/checkpoint.py', 'lab10/criteria.py', 'lab10/eval.py', 'lab10/gate.py', 'lab10/grade.py', 'lab10/helpers.py', 'lab10/mock_llm.py', 'lab10/ops.py', 'lab10/tools.py', 'lab10/trace.py', 'lab10/world.py', 'tests/test_public.py'] |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ❌ | base có vấn đề: True; after sạch: False; ticket còn hỏng: không; trần còn vượt: ['hàng chờ: 36 ca bị ùn (chờ quá 60 phút hoặc hết ca chưa tới lượt)', 'chi phí mỗi ticket 11212đ > làm tay 10000đ', 'kho CT: mỗi ticket tốn 10634đ > làm tay 10000đ', 'kho DN: mỗi ticket tốn 10625đ > làm tay 10000đ', 'kho HCM: mỗi ticket tốn 10639đ > làm tay 10000đ', 'kho HN: mỗi ticket tốn 10645đ > làm tay 10000đ'] |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['model_override_rate', 'carrier_fault_rate', 'pii_block_attempt_rate', 'queue_stuck_rate']; sáng đèn: [('model_override_rate', 'before', 0.045455, 0.0), ('model_override_rate', 'after', 0.045455, 0.0), ('carrier_fault_rate', 'before', 0.509091, 0.865385), ('carrier_fault_rate', 'after', 0.5, 0.730769), ('queue_stuck_rate', 'before', 0.0, 0.692308), ('queue_stuck_rate', 'after', 0.0, 0.692308)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 1.0 | 1.0 | 1.0 |
| thời gian chờ trung bình (phút) | 107.4 | 107.4 | 107.4 |
| thời gian chờ lâu nhất (phút) | 216.0 | 216.0 | 216.0 |
| số ca bị ùn | 36 | 36 | 36 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 100 | 100 | 100 |
| chi phí mỗi ticket (đ) · làm tay | 11225 · 10000 | 11212 · 10000 | 11212 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 669 · 1500 | 669 · 1500 | 669 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -1432721 | -63021 | -63021 |
| ROI | -2.45 | -0.11 | -0.11 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 498000 · 2000000 | 282000 · 2000000 | 282000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 1369000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 1.0 |
| số kho đắt hơn làm tay | 4 | 4 | 4 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 35 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.8182; hoàn sai 1080000; oan 10; PII 0; chi phí 10652đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10634đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10634đ > làm tay |
| kho DN | pass 0.75; hoàn sai 4625000; oan 20; PII 0; chi phí 10650đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10625đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10625đ > làm tay |
| kho HCM | pass 0.9231; hoàn sai 1140000; oan 5; PII 0; chi phí 10647đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10639đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10639đ > làm tay |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10645đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10645đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10645đ > làm tay |
| hãng DNB | pass 0.8182; hoàn sai 2300000; oan 10; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.9091; hoàn sai 520000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 0.8889; hoàn sai 560000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.75; hoàn sai 3465000; oan 15; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.2273 | 0.2273 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 0 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 4202 · 10000 | 4202 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 670 · 1500 | 670 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 127562 | 127562 |
| ROI | 1.34 | 1.38 | 1.38 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 1.0 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2567đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2567đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

Niềm tin của nhân viên duyệt (after, gói nhìn thấy): **chưa đạt** · còn thiếu: chưa bật ghi chú giải thích quyết định (operations.decision_note); tỉ lệ kiểm mẫu dưới mức đã thống nhất (10%)

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- VƯỢT TRẦN: hàng chờ: 36 ca bị ùn (chờ quá 60 phút hoặc hết ca chưa tới lượt) (trên visible)
- VƯỢT TRẦN: chi phí mỗi ticket 11212đ > làm tay 10000đ (trên visible)
- VƯỢT TRẦN: kho CT: mỗi ticket tốn 10634đ > làm tay 10000đ (trên visible)
- VƯỢT TRẦN: kho DN: mỗi ticket tốn 10625đ > làm tay 10000đ (trên visible)
- VƯỢT TRẦN: kho HCM: mỗi ticket tốn 10639đ > làm tay 10000đ (trên visible)
- VƯỢT TRẦN: kho HN: mỗi ticket tốn 10645đ > làm tay 10000đ (trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: cost_per_ticket_vnd ≤ 7000 (thực tế 11212, trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: roi ≥ 0.3 (thực tế -0.11, trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: queue_stuck ≤ 0 (thực tế 36, trên visible)
- KHÔNG đủ căn cứ để chọn 'Tiếp tục'. Thu hẹp, Cải tiến thêm hoặc Dừng, kèm lý do và con số, vẫn là quyết định đạt.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2273 | 0.2273 | +0.0 |
| visible | pass_rate | 0.8654 | 1.0 | 1.0 | +0.1346 |
| visible | pass_k | 0.8654 | 1.0 | 1.0 | +0.1346 |
| visible | wrongful_refund_vnd | 6845000 | 0 | 0 | -6845000 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 35 | 0 | 0 | -35 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.0 | 0.1346 | 0.1346 | +0.1346 |
