import socket
import requests
import threading

# Function to get the meaning of a word from the API
def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url, timeout=5)  # Add a timeout of 5 seconds
        if response.status_code == 200:
            data = response.json()
            meanings = data[0]['meanings']
            result = []
            for meaning in meanings:
                part_of_speech = meaning['partOfSpeech']
                definitions = meaning['definitions']
                for definition in definitions:
                    result.append(f"{part_of_speech}: {definition['definition']}")
            return "\n".join(result)
        else:
            return "Không tìm thấy nghĩa cho từ này."
    except requests.exceptions.Timeout:
        return "API request timed out."
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle each client connection in a separate thread
def handle_client(conn, addr):
    print(f"Kết nối từ {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            word = data.decode()
            print(f"Nhận từ: {word}")
            meaning = get_meaning(word)
            conn.sendall(meaning.encode())

# Function to start the server and accept connections
def start_server(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server đang chạy trên {host}:{port}")
        while True:
            conn, addr = s.accept()
            # Handle each client in a new thread to improve performance
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_server()
