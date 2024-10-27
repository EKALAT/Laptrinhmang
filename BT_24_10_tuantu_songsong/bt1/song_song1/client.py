import socket

def client():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        a = int(input("Nhập số a: "))
        b = int(input("Nhập số b: "))
        s.sendall(f"{a},{b}".encode())
        data = s.recv(1024)
        print("Số nguyên tố trong khoảng a den b :", data.decode())

client()