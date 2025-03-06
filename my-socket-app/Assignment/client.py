import socket

def client_main():
    host = "127.0.0.1"  # Must match the server's IP
    port = 25000        # Must match the server's port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to the server. Type 'exit' to quit.")

        while True:
            message = input("Enter a number: ")
            if message.lower() == "exit":
                break

            s.sendall(message.encode())
            data = s.recv(1024)
            print("Server response:", data.decode())

if __name__ == "__main__":
    client_main()
