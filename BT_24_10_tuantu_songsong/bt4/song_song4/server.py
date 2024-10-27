import socket
import threading

def handle_client(conn):
    with conn:
        data = conn.recv(1024).decode()
        numbers = list(map(float, data.split(',')))
        max_number = max(numbers)
        conn.sendall(str(max_number).encode())

def server():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn,)).start()

server()