import socket

def send_word(word, host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(word.encode())
        data = s.recv(1024)
        print(f"Ý nghĩa của '{word}': {data.decode()}")

if __name__ == "__main__":
    word = input("Nhập từ cần kiểm tra ý nghĩa: ")
    send_word(word)
