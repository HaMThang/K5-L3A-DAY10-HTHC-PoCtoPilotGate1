# Transcript demo LAB 10 · Gate 1 · S8

**Thời lượng:** khoảng 5 phút  
**Dùng khi:** nhóm thực sự bốc thẻ S8. Số liệu dưới đây lấy từ `submission/runs/grade-report.md` đang có. Report đó báo FAIL ở integrity và visible; hãy chạy lại kiểm tra trước khi dùng số như kết quả cuối.

## 0:00–0:35 · Mở đầu

“Nhóm em trình bày Gate 1 cho trợ lý hoàn tiền LogiX-VN, theo thẻ sự cố S8. Mục tiêu không phải chứng minh câu trả lời của chatbot nghe hợp lý. Mục tiêu là xác định hệ thống có ghi hành động an toàn, vận hành được và đạt tiêu chí đã ký hay chưa. Nhóm ký tiêu chí trước khi xem kết quả, nên quyết định hôm nay phải dựa trên các ngưỡng đó.”

## 0:35–1:20 · Ba mốc

“Đây là ba mốc: `base` là hành vi ban đầu; `prepared` là cổng vòng 1 đã chốt trước khi biết sự cố; `after` là cấu hình sau khi xử lý S8. So sánh ba mốc giúp ta thấy cổng nào đã có tác dụng và sửa đổi nào tạo thêm thay đổi. Đồng thời, bộ nền kiểm tra rằng các ticket vốn đúng vẫn tiếp tục đúng.”

“Trong report hiện có, trên S8, tiền hoàn sai giảm từ 1.369.000 đồng ở base xuống 0 ở prepared; lỗi ghi oan cho hãng giảm từ 35 xuống 0. Đây là bằng chứng cổng vòng 1 đã đỡ được rủi ro trước khi biết thẻ. Nhưng prepared vẫn có 36 ca ùn, chờ lâu nhất 216 phút và nhân viên kiểm lại 100% quyết định tự động.”

## 1:20–2:10 · S8 và rủi ro con người

“Thẻ S8 nói trưởng ca bị ghi nhận là người duyệt các khoản mà chị không duyệt. Có mã gắn với ticket khác, mã hết hạn hoặc bị thu hồi, và khoản chi vượt hạn mức phê duyệt. Sau kiểm toán, nhân viên không còn tin trợ lý và kiểm tay mọi quyết định, kể cả khoản nhỏ.”

“Đây không chỉ là vấn đề model. Có rủi ro quyền hạn và dữ liệu approval; có rủi ro con người vì người đứng tên phải giải trình; và có rủi ro vận hành vì một người chỉ xử lý được khoảng sáu ca duyệt mỗi giờ. Khi tất cả bị kiểm tay, hàng chờ tăng và chi phí có thể vượt làm tay.”

## 2:10–3:15 · Cổng và monitor

“Trong `lab10/guards.py`, nhánh refund tính lại quyền lợi từ tracking và policy, rồi kiểm tra phê duyệt trước khi ghi. Với khoản vượt hạn mức tự động, approval không hợp lệ thì hệ thống chuyển người duyệt; approval hợp lệ vẫn có thể đi tiếp. Như vậy nhóm nhắm vào tính hợp lệ của quyền duyệt, thay vì chặn tất cả các khoản.”

“Trong `lab10/monitors.py`, nhóm đăng ký `queue_stuck_rate`, đo tỷ lệ ticket bị mắc trong hàng chờ. Report hiện có ghi 0 trên bộ nền và 0,692308 trên S8 prepared. Metric này giúp phát hiện tải bất thường; nó không tự giải quyết backlog.”

“Config hiện có ghi PIC, approver và các điều kiện dừng, nhưng `decision_note` vẫn là false, `review_sampling_pct` là 0 và `max_queue_wait_minutes` chưa được đặt. Vì thế phần quy trình xây dựng chưa hoàn chỉnh; report cũng chưa chứng minh nhân viên đã lấy lại niềm tin.”

## 3:15–4:15 · Đánh giá

“Về an toàn, report hiện có ghi tiền hoàn sai và lỗi hãng oan bằng 0 ở prepared/after. Về vận hành và kinh tế, kết quả chưa đạt: 36 ca ùn, chờ tối đa 216 phút, chi phí 11.212 đồng mỗi ticket so với 10.000 đồng làm tay, và ROI âm 0,11. Cả bốn kho đều có chi phí cao hơn làm tay.”

“Vì vậy cổng kỹ thuật đã giảm một số lỗi nhìn thấy, nhưng hệ thống chưa sẵn sàng chạy pilot toàn phạm vi. Cần giải quyết hàng chờ, ghi chú giải thích và cách lấy mẫu kiểm tra; sau đó chạy lại cả bộ thẻ lẫn bộ nền.”

## 4:15–5:00 · Quyết định và kết

“Report hiện có còn đỏ ở hàng chờ, chi phí và ROI; grade hiện tại còn báo FAIL ở integrity và visible. Vì vậy nhóm không thể kết luận Tiếp tục. Quyết định v2 phải là lựa chọn phù hợp với decision rule đã ký và report chạy mới nhất—Cải tiến thêm hoặc Thu hẹp có điều kiện nếu dữ liệu hỗ trợ. Nhóm sẽ ghi một lựa chọn nhất quán trong Phiếu C12, không để hai phương án cùng tồn tại.”

“Trước Gate 2, cần đo công suất duyệt thực tế theo ca và depot, thời gian chờ, chi phí nhân sự, tỷ lệ kiểm mẫu mà nhân viên chấp nhận, và độ chính xác của dữ liệu phê duyệt. Đây là dữ liệu mock, nên kết quả hôm nay chưa đủ để suy rộng sang vận hành thật.”

## Nếu bị hỏi

**Tại sao không chặn toàn bộ hoàn tiền?**  
“Vì như vậy sẽ chặn cả trường hợp hợp lệ, làm giảm độ phủ và có thể làm chi phí/ROI xấu hơn. Cổng nên chuyển người khi thiếu căn cứ hoặc vượt quyền tự động, đồng thời giữ đường đi cho phê duyệt hợp lệ.”

**Monitor có làm giảm hàng chờ không?**  
“Không. Monitor phát hiện và đo. Stop condition, điều phối người và giới hạn phạm vi mới là hành động vận hành.”

**Vì sao chưa Tiếp tục?**  
“Vì report còn vượt trần hoặc chưa đạt ngưỡng đã ký: hàng chờ, chi phí và ROI. Hơn nữa grade hiện có báo FAIL ở integrity và visible.”

**Cần thêm bằng chứng gì?**  
“Grade tươi với integrity đạt; regression và monitor đạt; xác nhận config/phiếu/report dùng cùng phiên bản; số đo pilot thật về tải, chi phí và kiểm soát của người duyệt.”

## Nhắc trước khi trình bày

- Chạy `python -m lab10.eval --suite base --stage after --note "demo: regression"`.
- Chạy `python -m lab10.eval --suite S8 --stage after --note "demo: S8 v2"`.
- Chạy `python -m lab10.grade --incident S8` và `python -m lab10.check_submission --collect`.
- Chỉ gọi bài là đạt nếu kết quả tươi xác nhận integrity, regression, monitor và đủ thành phần. Cập nhật transcript/Phiếu C12 bằng số mới; không đọc số cũ như kết quả mới.
