import socket

# Client configuration
HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

try:
    while True:
        message = input("Enter message: ")
        client.send(message.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")
        if message.lower() == "exit":
            break
finally:
    client.close()
