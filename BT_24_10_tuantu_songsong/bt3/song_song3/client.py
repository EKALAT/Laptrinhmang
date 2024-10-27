import socket

def client():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        numbers = input("Nhập chuỗi các số thực, cách nhau bởi dấu phẩy: ")
        s.sendall(numbers.encode())
        data = s.recv(1024)
        print("Chuỗi số đã sắp xếp:", data.decode())

client()