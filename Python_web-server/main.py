# Socket initialization
import socket

HOST_SERVER = "0.0.0.0"
HOST_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP protocol (SOCK_DGRAM)

#Settings to change behaviour of the socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding socket to server(ip adress and port)
server_socket.bind((HOST_SERVER, HOST_PORT)) # Acess from any machine

# Listening to requests
server_socket.listen(5)# maximum number of connections on queue
print("Listening on port 8080")