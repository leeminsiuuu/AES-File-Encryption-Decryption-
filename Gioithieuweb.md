Giới thiệu về web
Web làm về thuật toán mã hóa và giải mã AES-128,AES-192,AES-256

1.CHỨC NĂNG CỦA ỨNG DỤNG
-Giai mã lại file về lại dạng _txt
-Mã hóa lại file về dạng _aes

2.CÁCH THỨC HOẠT ĐỘNG CỦA WEB
-MÃ HÓA:
B1:Chúng ta sẽ chọn file chúng ta muốn mã hóa và nhớ là file có đuôi txt
B2: Chúng ta sẽ đặt mật khẩu cho file, mật khẩu sẽ dài từ 16,24 hoặc 32
B3: Bấm vào thực hiện và file sẽ tự dowload lại về folder mà chúng ta chọn

-GIẢI MÃ:
B1:Chúng ta sẽ chọn file chúng ta muốn mã hóa và nhớ là file có đuôi aes
B2: Chúng ta sẽ đặt mật khẩu cho file, mật khẩu sẽ dài từ 16,24 hoặc 32
B3: Bấm vào thực hiện và file sẽ tự dowload lại về folder mà chúng ta chọn

3.CÔNG NGHỆ SỬ DỤNG
Có 2 phần chính:
-HTML tích hợp cả css và json dùng để làm giao diện web cho dẹp và lung linh hơn
-Python: Đây là phần chính dùng để thực hiện các hoạt động chính của web như giải mã, mã hóa và thực hiện tải về máy của mình
3.1.Flask:
+ Đây là một framework web nhẹ cho Python, cho phép xây dựng ứng dụng web một cách nhanh chóng và dễ dàng. Trong đoạn mã, Flask được sử dụng để tạo ra server và xử lý các yêu cầu HTTP.
3.2.Crypto (PyCryptodome):
+ Thư viện này cung cấp các tính năng mã hóa và giải mã. Trong mã của bạn, AES (Advanced Encryption Standard) được sử dụng để mã hóa và giải mã các tệp. pad và unpad được sử dụng để đảm bảo dữ liệu có kích thước phù hợp với khối của AES.

3.3.File Handling:
+ Mã sử dụng các thao tác với tệp để lưu trữ tệp tải lên, mã hóa, và giải mã tệp. Thư viện os được sử dụng để quản lý các thư mục và đường dẫn.
3.4.HTTP Methods:
+ Mã sử dụng các phương thức HTTP, đặc biệt là POST, để xử lý các yêu cầu từ phía client.
3.5.Error Handling:
Một số thông báo lỗi được trả về cho người dùng nếu có điều gì đó không đúng, chẳng hạn như khóa mã hóa không hợp lệ hoặc không có tệp được chọn.

4.GIAO DIỆN CỦA WEB
GIẢI MÃ
![image](https://github.com/user-attachments/assets/9e96b4c5-4c32-45d7-ac58-cce055c032e5)
MÃ HÓA
![image](https://github.com/user-attachments/assets/17b4dd27-fe40-4c5e-a7ed-54d45d9f528b)
