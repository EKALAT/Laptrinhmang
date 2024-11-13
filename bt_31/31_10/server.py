import socket

HOST = '127.0.0.1'  # Địa chỉ IP của server
PORT = 12345 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Nhập số để gửi lên server
    num = input("Nhập số: ")

    # Gửi số đến server
    s.sendall(num.encode())
    
    # Nhận phản hồi từ server
    data = s.recv(1024).decode()
    print('Số đã nhận từ server là:', data)
