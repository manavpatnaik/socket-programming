# Basic server that sends a message to client on connecting

import socket

SERVER = socket.gethostname()
PORT = 1234
ADDR = (SERVER, PORT)

# Initialize the socket object as a connection oriented socket - TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to the server host and port
server.bind(ADDR)

# Listen for connections - max queue length => 7
server.listen(7)
print('Server started...')

# Accept client connections
while True:
    client, addr = server.accept()
    print(f'New connection: {addr}')
    
    # Encode the string to utf-8
    message = 'Thanks for connecting!'.encode('utf-8')
    client.send(message)

    client.close()

print('Server shutting down...')

