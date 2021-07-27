# Basic client program to connect to server and receive messages and display them

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
CHUNK_SIZE = 4 # 4 Bytes
while True:
    msg = client.recv(CHUNK_SIZE).decode('utf-8')
    if len(msg) <= 0:
        break
    print(msg)

print('Client received all data...')