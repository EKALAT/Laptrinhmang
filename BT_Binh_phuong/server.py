import socket
import threading

def handle_client(client_socket, addr):
    print(f"Kết nối từ: {addr}")
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        try:
            number = float(data)
            response = f"Bình phương của {number} là {number ** 2}"
        except ValueError:
            response = "Dữ liệu không phải là số hợp lệ."
        client_socket.send(response.encode('utf-8'))
    print(f"Đóng kết nối từ: {addr}")
    client_socket.close()

server_ip, port = '0.0.0.0', 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((server_ip, port))
server.listen(5)
print("Server đang lắng nghe...")

while True:
    client_socket, addr = server.accept()
    threading.Thread(target=handle_client, args=(client_socket, addr)).start()
