# Tạo socket cho client
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Localhost
port = 12345

# Kết nối đến server
client_socket.connect((host, port))

try:
    number = input("Nhập một số: ")
    client_socket.send(number.encode())
    result = client_socket.recv(1024).decode()
    print(f"Bình phương của số đó là: {result}")
finally:
    client_socket.close()