# Kịch bản demo LAB 10 · Gate 1 (thẻ S8)

> Dùng cho demo nhóm 5 phút. Thẻ trong repo và báo cáo hiện có là S8. Chỉ dùng kịch bản này nếu S8 đúng là thẻ nhóm đã bốc. Các số dưới đây lấy từ `submission/runs/grade-report.md` hiện có; report đó đang báo `FAIL` ở integrity và visible, nên cần chạy lại trên repo sạch/đúng trạng thái trước khi trình bày kết quả mới như kết quả cuối.

## Mục tiêu demo

Cho người nghe thấy chuỗi bằng chứng `base → prepared → after`: cổng vòng 1 xử lý được vấn đề nào, thẻ S8 làm lộ rủi ro con người/vận hành gì, nhóm đã thêm cổng/monitor gì, và vì sao quyết định Gate 1 phải theo các ngưỡng đã ký.

## Trước giờ demo

1. Xác nhận nhóm thật sự bốc S8; không mở hoặc trình bày thẻ khác.
2. Từ thư mục gốc repo, kiểm tra `git status --short`, đúng tiêu chí đã ký và bản chụp vòng 1 còn nguyên. Không sửa `acceptance_criteria.json`, `guards_round1.py`, `operating_gates.round1.json` hay lock files.
3. Cập nhật code/config v2 dự định trình bày. Không đổi số thử nghiệm trong lúc demo, hoặc nếu có thì phải hoàn nguyên và chạy lại toàn bộ kiểm tra.
4. Tạo báo cáo tươi sau khi chốt cấu hình:

```powershell
python -m lab10.eval --suite base --stage after --note "demo: regression"
python -m lab10.eval --suite S8 --stage after --note "demo: S8 v2"
python -m lab10.grade --incident S8
python -m lab10.check_submission --collect
```

5. Chỉ trình bày là kết quả cuối nếu grade có `1 integrity ✅`, `regression ✅`, `monitor ✅`, report phản ánh đúng hash code/config hiện tại, và lệnh gom bài in `ĐỦ THÀNH PHẦN`. Nếu còn FAIL, trình bày đó là trạng thái chưa đạt và nêu rõ việc cần hoàn tất; không che hoặc gọi FAIL là PASS.
6. Mở sẵn `submission/runs/grade-report.md`, báo cáo JSON mốc `base/prepared/after`, `lab10/guards.py`, `lab10/monitors.py`, `config/operating_gates.json`, và Phiếu C mục C12.

## Luồng trình bày 5 phút

| Thời gian | Người nói | Nội dung / vật chứng |
|---|---|---|
| 0:00–0:35 | Điều phối / Sản phẩm | Bối cảnh và tiêu chí quyết định đã ký; nhắc đây là Gate 1, không phải demo độ hay của chatbot. |
| 0:35–1:20 | Kỹ sư cổng | So sánh ba mốc base, prepared, after; chỉ ra cổng vòng 1 và thay đổi vòng 2 trong code. |
| 1:20–2:10 | Vận hành / Pháp lý | S8: mã duyệt sai scope/hết hạn/vượt hạn mức và phản hồi trưởng ca; ảnh hưởng tới tin cậy, hàng chờ, người chịu trách nhiệm. |
| 2:10–3:15 | Kỹ sư cổng | Mở trace ticket đại diện, chỉ `_valid_approval`/`_refund_gate`, decision note/kiểm mẫu ở config và monitor mới. |
| 3:15–4:15 | Sản phẩm + Vận hành | Đọc hiệu quả và chi phí, queue/ROI, các ngưỡng còn chưa đạt; nêu nhánh rủi ro còn hở. |
| 4:15–5:00 | Trưởng nhóm | Đọc quyết định v2 đúng theo report và acceptance criteria; nêu điều kiện trước khi mở rộng/pilot tiếp. |

## Transcript gợi ý

### 0:00–0:35 · Bối cảnh và tiêu chí

“Nhóm em trình bày Gate 1 cho trợ lý hoàn tiền LogiX-VN, với thẻ sự cố S8. Mục tiêu hôm nay không phải chứng minh chatbot trả lời nghe hợp lý; mục tiêu là kiểm tra hệ thống có thể ghi hành động an toàn, vận hành được và đạt các tiêu chí đã ký hay chưa. Nhóm ký tiêu chí trước khi chạy đánh giá. Vì vậy quyết định cuối phải theo report và các ngưỡng đó.”

### 0:35–1:20 · Ba mốc đánh giá

“Đây là ba mốc. `base` cho thấy hành vi ban đầu. `prepared` chạy với cổng vòng 1 đã chốt trước khi biết sự cố. `after` chạy với sửa đổi sau khi nhận S8. Ta so cùng bộ thẻ và bộ nền để thấy vừa xử lý sự cố vừa giữ các ca vốn đúng.”

“Trong báo cáo hiện có, mốc prepared giảm lỗi hoàn sai trên S8 từ 1.369.000 đồng xuống 0 và lỗi hãng oan từ 35 xuống 0. Đó là bằng chứng cổng vòng 1 đã chặn được một phần rủi ro tài chính/đối tác trước khi biết S8. Nhưng prepared vẫn có 36 ca ùn, thời gian chờ tối đa 216 phút và nhân viên kiểm lại 100% quyết định tự động.”

### 1:20–2:10 · Thẻ S8 và yếu tố con người

“Thẻ S8 ghi nhận trưởng ca nói mình bị đứng tên duyệt khoản mà không hề duyệt: có mã gắn ticket khác, mã hết hạn hoặc thu hồi, và khoản vượt giới hạn duyệt. Sau kiểm toán, nhân viên mất niềm tin và kiểm tay mọi quyết định, kể cả khoản nhỏ. Đây không chỉ là lỗi model. Có nhánh quyền hạn và dữ liệu phê duyệt; có nhánh vận hành khi một người chỉ duyệt được sáu ca mỗi giờ; và có nhánh niềm tin vì thiếu giải thích cho quyết định.”

“Vì thế câu hỏi của nhóm là: hệ thống xác thực quyền duyệt theo đơn, trạng thái, ngày hết hạn và hạn mức chưa; đồng thời người duyệt có đủ căn cứ để kiểm nhanh và có quyền tiếp quản ở đâu?”

### 2:10–3:15 · Cổng và monitor

“Ở `lab10/guards.py`, cổng refund đọc đơn và policy từ nguồn dữ liệu chuẩn, tính lại entitlement, rồi kiểm mã phê duyệt. Nếu phê duyệt không hợp lệ cho khoản vượt hạn mức tự động, lệnh không được ghi tự động mà chuyển người. Một phê duyệt hợp lệ như S8-05 vẫn được phép xử lý; nhóm không chặn tất cả.”

“Ở `config/operating_gates.json`, có PIC, approver và điều kiện dừng khi approval sai hoặc hàng chờ quá 60 phút. Ở `lab10/monitors.py`, nhóm thêm `queue_stuck_rate` để nhận biết phần trăm ticket mắc trong hàng chờ. Trong report hiện có, chỉ số là 0 trên bộ nền và 0,692308 trên S8 prepared. Nó báo được tải vận hành khác thường, nhưng tự nó không giải quyết thiếu công suất hay phục hồi lòng tin.”

### 3:15–4:15 · Đánh giá thương mại và vận hành

“Cổng giảm sai sót kỹ thuật nhưng chưa làm cho pilot khả thi. Report hiện có cho S8 prepared/after: 36 ca ùn, chờ cao nhất 216 phút; chi phí 11.212 đồng mỗi ticket so với 10.000 đồng làm tay; ROI âm 0,11. Bốn kho đều có chi phí/ticket cao hơn xử lý tay. Đây là các ngưỡng còn đỏ, nên không thể kết luận tiếp tục như hiện trạng.”

“Rủi ro còn lại là tải thực tế theo giờ và khả năng nhân viên chấp nhận quy trình kiểm mẫu. `queue_stuck_rate` là tín hiệu phát hiện; quyết định dừng nhận thêm/thu hẹp mới là hành động vận hành. Trước khi chạy thật cần xác minh note giải thích, tỉ lệ kiểm mẫu, SLA người duyệt và chi phí đầy đủ.”

### 4:15–5:00 · Quyết định v2

“Dựa trên report hiện có, nhóm không chọn Tiếp tục toàn phạm vi: còn vượt trần hàng chờ và chi phí, ROI chưa đạt ngưỡng đã ký. Quyết định v2 đề xuất là **Cải tiến thêm** nếu tiêu chí đã ký cho phép và nhóm có thể giữ pilot ở chế độ kiểm soát; nếu phải đưa ra quyết định vận hành ngay thì **Thu hẹp** tới phạm vi có số liệu đạt, chuyển phần còn lại cho người. Nhóm ghi rõ lựa chọn thật trong Phiếu C12, cùng ba mã run, ngưỡng đã ký và ngày đánh giá lại.”

“Bằng chứng của nhóm có giới hạn: đây là dữ liệu mô phỏng. Trước Gate 2 cần đo tải theo depot/ca, thời gian xử lý và chi phí nhân sự thực tế, tỉ lệ kiểm mẫu mà nhân viên chấp nhận, và xác nhận approval binding với ticket/đơn/khách. Sau đó mới xem xét mở rộng.”

## Bảng đánh giá để chiếu

| Trục đánh giá | Bằng chứng trong report hiện có | Nhận định demo |
|---|---|---|
| Tính toàn vẹn | Grade hiện có báo `1 integrity ❌`, nhiều file khóa bị đổi | Chưa đủ điều kiện tuyên bố bài nộp hợp lệ; cần xác minh trạng thái repo/hash và chạy grade tươi. |
| An toàn khoản hoàn | S8 prepared/after: hoàn sai 0; cổng kiểm approval trong `_refund_gate` | Tốt trên ca nhìn thấy; còn cần kiểm thử hidden và xác thực ticket/customer/status đầy đủ. |
| Bảo vệ hãng / dữ liệu | S8 prepared/after: lỗi hãng oan 0; PII leak 0 | Tín hiệu tốt trên bộ thử; không chứng minh rủi ro bằng 0 trong pilot thật. |
| Hồi quy | Report cũ báo pass_rate bộ nền 0,9909 → 1,0, không ca mới hỏng | Đạt trên report đó; phải chạy lại trên code/config hiện tại. |
| Vận hành | 36 ca ùn; chờ tối đa 216 phút; 1 người, 6 ca/giờ | Không đạt SLA hiện có; phải thu hẹp/dừng nhận thêm hoặc cải tiến năng lực. |
| Kinh tế | 11.212đ/ticket so với 10.000đ làm tay; ROI −0,11 | Chưa đạt; không tiếp tục toàn phạm vi. |
| Niềm tin người duyệt | Grade cũ: chưa đạt; thiếu decision note, sampling 10% chưa thoả | Cần hiển thị căn cứ và đồng thuận quy trình lấy mẫu trước khi bớt kiểm tay. |
| Monitor | `queue_stuck_rate`: base 0; S8 0,692308 | Phát hiện sự cố; không thay thế gate/đội xử lý. |

## Câu hỏi phản biện dự kiến

- **Vì sao không chặn mọi khoản hoàn?** Vì sẽ phá độ phủ và ROI, đồng thời chặn cả ca hợp lệ. Gate chỉ chuyển người khi không đủ căn cứ hoặc vượt quyền tự động.
- **Approval hợp lệ phải khớp những gì?** Ít nhất order, ticket, người/khách nếu dữ liệu hỗ trợ, trạng thái còn hiệu lực, thời hạn và max amount; phải xác minh đúng schema dữ liệu thẻ.
- **Monitor queue_stuck_rate có sửa được hàng chờ không?** Không. Nó phát hiện/đo; config stop condition và thao tác thu hẹp/dừng nhận thêm là bước vận hành.
- **Tại sao không chọn Tiếp tục?** Report còn đỏ ở hàng chờ, chi phí và ROI; tiêu chí lab yêu cầu quyết định khớp bằng chứng.
- **Điều gì cần đo ở pilot thật?** Công suất người duyệt theo ca/depot, chi phí nhân sự, thời gian chờ, tỉ lệ kiểm mẫu được chấp nhận và độ chính xác của dữ liệu approval.

## Chốt trước khi nói

Report `submission/runs/grade-report.md` đang là bản FAIL: integrity ❌ và visible ❌; phần trust cũng chưa đạt. Transcript trên dùng các con số đó như **kết quả hiện có**, không trình bày chúng như kết quả đã qua. Chạy lại báo cáo sau khi giải quyết integrity và đồng bộ code/config/submission; sửa transcript và Phiếu C12 theo kết quả mới. Không thay báo cáo bằng số ước tính.
