import socket

def is_digit_sum_15(n):
    """Kiểm tra xem tổng các chữ số của n có bằng 15 hay không."""
    return sum(int(digit) for digit in str(n)) == 15

def server_sequential():
    """Khởi động máy chủ để phục vụ tuần tự."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12346))
        s.listen()
        print("Máy chủ đang lắng nghe...")
        while True:
            conn, addr = s.accept()  # Chấp nhận kết nối mới
            print('Kết nối từ', addr)
            data = conn.recv(1024)  # Nhận dữ liệu từ khách hàng
            if data:
                a, b = map(int, data.decode().split())  # Giải mã và chuyển đổi thành số nguyên
                result = [str(i) for i in range(a, b + 1) if is_digit_sum_15(i)]  # Tính các số có tổng chữ số bằng 15
                if result:
                    response = " ".join(result)  # Chuẩn bị phản hồi
                else:
                    response = "Không tìm thấy số nào có tổng chữ số bằng 15."
                conn.sendall(response.encode())  # Gửi kết quả trở lại khách hàng
            conn.close()  # Đóng kết nối với khách hàng

if __name__ == "__main__":
    server_sequential()
