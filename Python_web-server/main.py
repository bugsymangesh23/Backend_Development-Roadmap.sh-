# Socket initialization
import socket
import time

HOST_SERVER = "0.0.0.0"
HOST_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #UDP protocol (SOCK_DGRAM)

#Settings to change behaviour of the socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding socket to server(ip adress and port)
server_socket.bind((HOST_SERVER, HOST_PORT)) # Acess from any machine

# Listening to requests
server_socket.listen(5)# maximum number of connections on queue

print(f"Listening on port {HOST_PORT}...")
# Infinite loop to prevent error loading
while True:
    try:
    # Accepting connection requets(blocking and non-blocking)
        client_socket, client_address = server_socket.accept()
        print(client_address)
        print(client_socket)
    except:
        time.sleep(1)
        print("Error loading page")