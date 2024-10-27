import socket

def client():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        number = int(input("Nhập một số nguyên: "))
        s.sendall(str(number).encode())
        data = s.recv(1024)
        print("Tổng các chữ số:", data.decode())

client()