import socket

# Thiết lập thông tin kết nối
HOST = '127.0.0.1'  # Địa chỉ IP của server
PORT = 65432        # Cổng sử dụng

# Tạo socket cho server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Gắn địa chỉ và cổng cho socket
    s.listen()            # Chờ kết nối từ client
    print(f"Server đang lắng nghe trên {HOST}:{PORT}...")
    
    # Chấp nhận kết nối từ client
    conn, addr = s.accept()
    with conn:
        print('Kết nối từ', addr)
        data = conn.recv(1024).decode()  # Nhận dữ liệu từ client
        num1, num2 = map(int, data.split())  # Tách 2 số và chuyển sang kiểu int
        result = num1 + num2  # Tính tổng
        conn.sendall(str(result).encode())  # Gửi kết quả lại cho client
