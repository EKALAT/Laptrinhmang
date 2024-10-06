import socket

# Thiết lập thông tin kết nối đến server
HOST = '127.0.0.1'  # Địa chỉ IP của server
PORT = 65432        # Cổng sử dụng

# Tạo socket cho client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Kết nối đến server
    
    # Nhập 2 số từ người dùng
    num1 = input("Nhập số thứ nhất: ")
    num2 = input("Nhập số thứ hai: ")
    
    # Gửi 2 số đến server
    s.sendall(f"{num1} {num2}".encode())
    
    # Nhận kết quả từ server
    data = s.recv(1024).decode()
    print('Tổng hai số là:', data)
