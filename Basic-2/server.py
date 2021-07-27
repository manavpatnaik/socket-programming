# A ping pong server
# If anything other than ping is sent it will echo it
import socket

SERVER = socket.gethostname()
PORT = 1234
ADDR = (SERVER, PORT)

# Initialize the socket object as a connection oriented socket - TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to the server host and port
server.bind(ADDR)

# Listen for connections - max queue length => 5
server.listen(5)
print('Server started...')

# Accept client connection - Only one connection to ping pong with
client, addr = server.accept()
while True:
    print(f'New connection: {addr}')

    recv_msg = client.recv(1024).decode('utf-8')

    if recv_msg == 'exit':
        client.close()
        break

    if recv_msg == 'ping':
        # Encode the string to utf-8
        message = 'pong!!!'.encode('utf-8')
    else:
        message = recv_msg.encode('utf-8')
    
    client.send(message)


print('Server shutting down...')
