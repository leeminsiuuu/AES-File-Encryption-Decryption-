from flask import Flask, render_template, request, send_file
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

# Tạo thư mục nếu chưa có
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Hàm mã hóa AES
def encrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        data = f.read()
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    output_path = os.path.join(app.config["OUTPUT_FOLDER"], "encrypted_file.aes")
    with open(output_path, "wb") as f:
        f.write(iv + encrypted_data)
    return output_path

# Hàm giải mã AES
def decrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        encrypted_data = f.read()
    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
    output_path = os.path.join(app.config["OUTPUT_FOLDER"], "decrypted_file")
    with open(output_path, "wb") as f:
        f.write(decrypted_data)
    return output_path

@app.route("/")
def index():
    return render_template("index.html")  # Trả về giao diện HTML

@app.route("/process", methods=["POST"])
def process_file():
    if "file" not in request.files or not request.form.get("key"):
        return "Vui lòng chọn file và nhập khóa mã hóa!", 400

    file = request.files["file"]
    key = request.form.get("key")

    # Kiểm tra độ dài của khóa mã hóa
    if len(key) not in [16, 24, 32]:
        return "Khóa phải có độ dài 16, 24 hoặc 32 ký tự!", 400

    operation = request.form.get("operation")
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # Xử lý mã hóa hoặc giải mã
    if operation == "encrypt":
        output_path = encrypt_file(file_path, key)
        return send_file(output_path, as_attachment=True)

    elif operation == "decrypt":
        output_path = decrypt_file(file_path, key)
        return send_file(output_path, as_attachment=True)

    else:
        return "Yêu cầu không hợp lệ!", 400

if __name__ == "__main__":
    app.run(debug=True)