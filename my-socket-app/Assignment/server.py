import socket
import threading
from even_odd import check_even_odd

def handle_client(conn, addr):
    """
    Handle client connection.
    Receive data from the client, check if it's even or odd, and send the result back.
    """
    print(f"Client {addr} connected.")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            message = data.decode().strip()
            try:
                number = int(message)
                result = check_even_odd(number)
            except ValueError:
                result = f"Invalid input '{message}'. Please enter a valid number."

            conn.sendall(result.encode())
    print(f"Client {addr} disconnected.")

def server_main():
    host = ""        # Listen on all available network interfaces (0.0.0.0)
    port = 25000     # Port number

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Prevent port binding issues
        s.bind((host, port))
        s.listen()
        print(f"Server listening on port {port}")

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
            print(f"Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    server_main()
