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

# Infinite loop to listen for multiple connections
while True:
    # Accepting connection requets(blocking and non-blocking)
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode() #get user requests
    print(request)
    headers = request.split("\n") # Split request with a new line
    first_header_components = headers[0].split()

    http_methods = first_header_components[0]
    path = first_header_components[1]

    # handle all the http http_methods
    if http_methods == 'GET':
    # Check path
        if path == '/':
            file_input = open('index.html')
            content = file_input.read()
            file_input.close()

            # HTTP RESPONSE
            # headers
            # message-body
            response = 'HTTP/1.1 200 OK \n\n' + content
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\n'
         # send response to client
        client_socket.sendall(response.encode())
        client_socket.close()