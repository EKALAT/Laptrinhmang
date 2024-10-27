import socket

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
            numbers = list(map(float, data.split(',')))
            max_number = max(numbers)
            conn.sendall(str(max_number).encode())

server()