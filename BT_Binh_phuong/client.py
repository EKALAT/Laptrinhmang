import socket

server_ip = '127.0.0.1'
port = 5000

# Khởi tạo socket và kết nối tới server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, port))

while True:
    # Nhập dữ liệu từ người dùng
    data = input('Nhập số để tính bình phương (hoặc "exit" để thoát): ')
    if data.lower() == "exit":
        print("Đã thoát.")
        break

    # Gửi dữ liệu tới server
    client.send(data.encode('utf-8'))

    # Nhận kết quả từ server
    response = client.recv(1024).decode('utf-8')
    print('Phản hồi từ server:', response)

# Đóng kết nối sau khi hoàn tất
client.close()
