import socket
import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def handle_client(conn):
    with conn:
        data = conn.recv(1024).decode()
        a, b = map(int, data.split(','))
        primes = [str(num) for num in range(a, b + 1) if is_prime(num)]
        conn.sendall(','.join(primes).encode())

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