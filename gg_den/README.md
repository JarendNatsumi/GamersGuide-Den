# Gamers Guide (GG Den)

Website chia sẻ **guide** và **review game**, xây dựng bằng Django, SQLite, HTML5 và CSS3. Thiết kế ưu tiên máy tính, có giao diện sáng/tối. Bài viết công khai có thể đọc mà không cần đăng nhập.

## Tính năng
- Trang chủ hiển thị bài viết mới nhất, tìm kiếm theo tiêu đề/nội dung và lọc Guide / Review.
- Trang chi tiết bài viết, ảnh đại diện bài viết, nội dung có định dạng đoạn văn.
- Đăng ký, đăng nhập, đăng xuất.
- Thành viên đã đăng nhập có thể tạo, sửa, xóa bài của chính mình.
- Mỗi bài là **Guide** hoặc **Review**; trạng thái bản nháp/đã xuất bản.
- Chọn ảnh bìa (không bắt buộc).
- Chế độ sáng/tối, lưu lựa chọn trong trình duyệt.
- Django Admin để quản lý tài khoản và bài viết.
- SQLite được cấu hình sẵn; không cần cài database riêng.

## Yêu cầu
- Windows 10/11
- Python 3.11 trở lên (khuyến nghị Python 3.12)
- Internet trong lần cài đầu để cài Django và Pillow

## Cài đặt trên Windows
1. Giải nén `GG_Den.zip` vào thư mục bạn muốn.
2. Mở thư mục `gg_den`.
3. Nhấp đúp `setup.bat`. Script sẽ tạo môi trường ảo `.venv`, cài thư viện và tạo database SQLite.
4. Sau khi hoàn tất, chạy `run.bat`.
5. Mở trình duyệt tại http://127.0.0.1:8000/

Nếu Windows không cho chạy file `.bat`, mở PowerShell tại thư mục dự án và chạy:
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

## Tạo tài khoản quản trị
Mở PowerShell tại thư mục dự án:
```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```
Sau đó truy cập http://127.0.0.1:8000/admin/ và đăng nhập.

## Đăng bài
1. Đăng ký tài khoản hoặc đăng nhập.
2. Chọn **Viết bài** trên thanh điều hướng.
3. Chọn loại bài: Guide hoặc Review, nhập tiêu đề, tóm tắt và nội dung.
4. Có thể tải ảnh bìa và chọn xuất bản hoặc lưu nháp.
5. Bài đã xuất bản sẽ hiển thị công khai; bài nháp chỉ chủ bài và quản trị viên xem được.

## Cấu trúc thư mục
```text
gg_den/
├── manage.py
├── requirements.txt
├── setup.bat
├── run.bat
├── ggden/                 # Cấu hình Django
├── guides/                # Model, view, form, URL
├── templates/             # HTML templates
├── static/css/             # CSS
├── static/js/              # Chế độ sáng/tối
└── media/                  # Ảnh tải lên (tạo tự động)
```

## Lưu ý
- Đây là dự án local để học tập/demo. Trước khi triển khai lên Internet, cần cấu hình `DEBUG=False`, `ALLOWED_HOSTS`, HTTPS, bảo vệ media upload và dùng cơ chế lưu trữ phù hợp.
- Nội dung bài viết được hiển thị dưới dạng văn bản thuần theo từng dòng; không cho phép HTML tùy ý để giảm rủi ro XSS.
- SQLite file `db.sqlite3` sẽ được tạo sau khi chạy migration.
