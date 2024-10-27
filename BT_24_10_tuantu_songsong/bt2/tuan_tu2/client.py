import socket

def client_sequential():
    """Kết nối đến máy chủ và gửi số."""
    a = int(input("Nhập số đầu tiên (a): "))  # Nhập số đầu tiên từ người dùng
    b = int(input("Nhập số thứ hai (b): "))  # Nhập số thứ hai từ người dùng
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12346))  # Kết nối đến máy chủ
        s.sendall(f"{a} {b}".encode())  # Gửi số đến máy chủ
        data = s.recv(1024)  # Nhận phản hồi từ máy chủ
        print('Nhận được:', data.decode())  # In ra dữ liệu nhận được

if __name__ == "__main__":
    client_sequential()
