# Socket initialization
import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP protocol (SOCK_DGRAM)

#Settings to change behaviour of the socket
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)