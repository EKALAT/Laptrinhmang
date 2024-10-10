import socket

# Function to send stock symbol to the server
def send_stock_symbol(symbol, host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(symbol.encode())
        data = s.recv(1024)
        print(f"Nhận được từ server: {data.decode()}")

if __name__ == "__main__":
    symbol = input("Nhập mã chứng khoán: ")
    send_stock_symbol(symbol)
