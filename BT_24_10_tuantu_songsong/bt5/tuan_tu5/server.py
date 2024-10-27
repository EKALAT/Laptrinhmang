import socket

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def server():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024).decode()
            total = digit_sum(int(data))
            conn.sendall(str(total).encode())

server()