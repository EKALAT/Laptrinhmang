import socket

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
            a, b = map(int, data.split(','))
            primes = [str(num) for num in range(a, b + 1) if is_prime(num)]
            conn.sendall(','.join(primes).encode())

server()