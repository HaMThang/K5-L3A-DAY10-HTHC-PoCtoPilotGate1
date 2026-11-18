# Team

## Thông tin nhóm

- Tên nhóm: `HTHC`
- Lớp: `L3A`
- Repo của bàn: K5-L3A-DAY10-HTHC-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |   Lê Gia Hưng        | 2A202603706    |Kỹ sư cổng 1 · giữ máy chính     |     Trưởng nhóm         |
|   2 |    Hà Minh Thắng       |   2A202603676   |Kỹ sư cổng 2 · trace, test, monitor     |            |
|   3 |   Nguyễn Thế Hoàng        |  2A202603718    |	Sản phẩm và kinh doanh     |             |
|   4 |  Đặng Đức Cương         | 2A202603680     |Vận hành và pháp lý     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## LeGiaHung-2A202603706

### Phần việc phụ trách

Người A · Kỹ sư cổng 1, giữ máy chính. Phụ trách câu 2.1, 2.6, chốt cổng vòng 1, câu 3.0 và phần code 3.5; quản lý các lần chạy `eval`/`grade` theo phân công. File chính: `lab10/guards.py`.

### Đóng góp cụ thể

- Triển khai và duy trì các cổng xử lý trong `lab10/guards.py` để ngăn hoàn tiền sai và ghi lỗi hãng oan; phối hợp kiểm tra hành vi sau khi nhận config của C và D.
- Chạy các mốc base/prepared/after và grade sự cố S8 trên máy chính, cung cấp mã run và số liệu để bàn điền B0, C0/C1 và ra quyết định.
- Phối hợp xử lý nguyên nhân kỹ thuật S8; các ca S8-01/02/03 bị chuyển người khi approval không đạt điều kiện, trong khi ca hợp lệ S8-05 vẫn được xử lý.

### Bằng chứng

`lab10/guards.py`; `templates/form-b-evaluation-gates.md` (B0, B1, B7.1); `templates/form-c-incident.md` (C0, C1, C7); các mốc `R-S8-before-20261118-172628-0d3d70`, `R-S8-prepared-20261118-172628-0d3d70`, `R-S8-after-20261118-172628-0d3d70` và grade `R-S8-grade-20261118-172627-0d3d70`.

### Exit ticket

Thành viên tự bổ sung điều đã học và điều còn chưa chắc.

## HaMinhThang-2A202603676

### Phần việc phụ trách

Người B · Kỹ sư cổng 2, trace, test và monitor. Phụ trách câu 1.3, 2.2, 2.7, 2.8, 3.1 (trace và C2), 3.6 (C8); file chính: `lab10/monitors.py`.

### Đóng góp cụ thể

- Hoàn thành nội dung câu 1.3 và các phần B2, B7.2/B7.3 theo phân công; dùng trace để chỉ ra lỗi theo từng ticket thay vì chỉ dựa vào kết quả tổng hợp.
- Đối chiếu approval trong sự cố S8 với `incidents/S8/world_patch.json`, ghi các lỗi khác nguồn, tác hại và hướng xử lý ở C2; dẫn fault tree C6 cùng bàn.
- Bổ sung monitor `queue_stuck_rate` vào `lab10/monitors.py` và điền C8. Chỉ số phân biệt bộ nền (0.000000) với S8 (0.692308), giúp phát hiện ùn hàng chờ nhưng không tự xác định nguyên nhân.

### Bằng chứng

`lab10/monitors.py`; `templates/form-a-criteria.md` (1.3); `templates/form-b-evaluation-gates.md` (B2, B7.2, B7.3); `templates/form-c-incident.md` (C2, C6, C8); trace `S8-01@11`, `S8-02@11`, `S8-03@11` và ca hợp lệ `S8-05@11`.

### Exit ticket

Thành viên tự bổ sung điều đã học và điều còn chưa chắc.

## NguyenTheHoang-2A202603718

### Phần việc phụ trách

Người C · Sản phẩm và kinh doanh. Phụ trách câu 1.1, 1.6, 2.3, 2.9, B8 (v1), 3.2 và C12 (v2); giữ `config/acceptance_criteria.json` và phần `business` trong `config/operating_gates.json`.

### Đóng góp cụ thể

- Xây dựng tiêu chí chấp nhận và lý do cho các ngưỡng kinh doanh; hoàn thành phần bản đồ dữ liệu/drift, các cổng business và bằng chứng quyết định v1 theo phân công.
- Đối chiếu chi phí/ticket, ROI, tổng tiền hoàn và phạm vi pilot với report; ghi nhận các trần còn vi phạm sau S8 để làm căn cứ cho quyết định v2.
- Chịu trách nhiệm chốt nội dung kinh doanh trong C7/C12, gồm phạm vi pilot, giới hạn và điều kiện cần xem lại trước khi tiếp tục.

### Bằng chứng

`config/acceptance_criteria.json`; phần `business` của `config/operating_gates.json`; `templates/form-a-criteria.md` (1.1, 1.6); `templates/form-b-evaluation-gates.md` (B3, B7.4, B8); `templates/form-c-incident.md` (C5, C7, C12); report S8 trong `runs/`.

### Exit ticket

Thành viên tự bổ sung điều đã học và điều còn chưa chắc.

## DangDucCuong-2A202603680

### Phần việc phụ trách

Người D · Vận hành và pháp lý. Phụ trách câu 1.2, 1.4, 2.4 (B4/B5), 2.10 (B7.5/B7.6), C3, C4, 3.3 và 3.7 (C9–C11); giữ phần `operations`/`legal` trong `config/operating_gates.json` và `submission/submission.json`.

### Đóng góp cụ thể

- Ghi mục tiêu vận hành/pháp lý, HAZOP và checklist B4/B5; đề xuất PIC, người duyệt, kênh báo tin, điều kiện dừng và runbook theo các cổng vận hành.
- Hoàn thiện phân tích theo thẻ S8 ở C3/C4 và cập nhật fault tree sau sửa, risk register, checklist cùng runbook sau sự cố ở C9–C11.
- Điền thông tin gói nộp trong `submission/submission.json` theo quyết định của bàn; phối hợp kiểm tra các điều kiện con người và vận hành còn thiếu.

### Bằng chứng

Phần `operations`/`legal` của `config/operating_gates.json`; `submission/submission.json`; `templates/form-b-evaluation-gates.md` (B4, B5, B7.5, B7.6); `templates/form-c-incident.md` (C3, C4, C9–C11).

### Exit ticket

Thành viên tự bổ sung điều đã học và điều còn chưa chắc.
