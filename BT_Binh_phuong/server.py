import socket
import threading
# Hàm này xử lý kết nối với từng client
def kk(client_socket, addr):
    print(f"Kết nối từ: {addr}")  # In ra địa chỉ của client khi kết nối
    while True:
        # Nhận dữ liệu từ client (tối đa 1024 byte)
        data = client_socket.recv(1024).decode('utf-8')
        # Nếu không nhận được dữ liệu, tức là client đã ngắt kết nối, thoát khỏi vòng lặp
        if not data:
            break
        try:
            # Cố gắng chuyển dữ liệu nhận được thành số thực
            number = float(data)
            # Nếu thành công, tính bình phương của số đó
            response = f"Bình phương của {number} là {number ** 2}"
        except ValueError:
            # Nếu dữ liệu không phải là số hợp lệ, gửi thông báo lỗi
            response = "Dữ liệu không phải là số hợp lệ."

        # Gửi kết quả (bình phương hoặc thông báo lỗi) trở lại cho client
        client_socket.send(response.encode('utf-8'))
    
    # Sau khi client ngắt kết nối, in ra thông báo và đóng kết nối với client
    print(f"Đóng kết nối từ: {addr}")
    client_socket.close()
# Địa chỉ IP và cổng của server
server_ip, port = '0.0.0.0', 5000
# Tạo một socket cho server sử dụng giao thức IPv4 và TCP (streaming)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Cho phép server tái sử dụng địa chỉ đã được bind (giúp tránh lỗi khi khởi động lại server)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind server với địa chỉ IP và cổng đã chỉ định
server.bind((server_ip, port))

# Bắt đầu lắng nghe các kết nối đến (tối đa 5 client có thể đợi trong hàng đợi)
server.listen(5)
print("Server đang lắng nghe...")

# Vòng lặp vô hạn để liên tục chấp nhận kết nối từ client
while True:
    # Chấp nhận kết nối từ client
    client_socket, addr = server.accept()
    # Tạo một thread mới để xử lý client, cho phép nhiều client kết nối đồng thời
    threading.Thread(target=kk, args=(client_socket, addr)).start()
