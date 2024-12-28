import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

# Function to handle each client
def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    while True:
        try:
            # Receive data from client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print(f"[DISCONNECT] {address} disconnected.")
                break
            
            print(f"[{address}] {data}")
            
            # Send a response back to the client
            client_socket.send("ACK".encode('utf-8'))
        except ConnectionResetError:
            print(f"[ERROR] Connection with {address} lost.")
            break

    client_socket.close()

# Main server function
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    
    while True:
        client_socket, address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
