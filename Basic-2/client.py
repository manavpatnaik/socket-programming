# Client that sends messages to server

import socket

# Define address and hostname of server to connect
SERVER = socket.gethostname()
PORT = 1234
ADDR = (SERVER, PORT)

# Initialize a socket object, connectionless - TCP - SOCK_STREAM
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(ADDR)

# Receive message:
CHUNK_SIZE = 1024 # 1024 Bytes
while True:
    send_msg = input()
    client.send(send_msg.encode('utf-8'))
    
    if send_msg == 'exit':  
        break

    msg = client.recv(CHUNK_SIZE).decode('utf-8')
    print('Server:', msg)

print('Client received data...')