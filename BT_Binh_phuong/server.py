import socket
import threading

def kk(client_socket, addr):
    print(f"Kết nối từ: {addr}")
    while (data := client_socket.recv(1024).decode('utf-8')):
        try:
            number = float(data)
            response = f"Bình phương của {number} là {number ** 2}"
        except ValueError:
            response = "Dữ liệu không phải là số hợp lệ."
        client_socket.send(response.encode('utf-8'))
    
    print(f"Đóng kết nối từ: {addr}")
    client_socket.close()

# Thiết lập server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5000))
server.listen(5)
print("Server đang lắng nghe...")

while True:
    client_socket, addr = server.accept()
    threading.Thread(target=kk, args=(client_socket, addr)).start()
