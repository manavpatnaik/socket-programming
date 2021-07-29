# There are 10 rows of data in the csv file
# Client can send 2 numbers after connecting: start & end
# Those will the rows (start to end) that will be sent to the server
# Request: Rows from start to end, Reponse: Data from csv file rows start to end

import socket
import threading
import pandas as pd

df = pd.read_csv('./data.csv')

HOST = socket.gethostname()
PORT = 5001
ADDR = (HOST, PORT)
CHUNK_SIZE = 64
FORMAT = 'utf-8'
DISCONNECT = 'DISCONNECT'

# Init socket obj
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address
server.bind(ADDR)

# Method to serve data to client


def serve_client(client, addr):
    connected = True
    while connected:
        start = client.recv(CHUNK_SIZE).decode(FORMAT)
        end = client.recv(CHUNK_SIZE).decode(FORMAT)

        if start == DISCONNECT or end == DISCONNECT:
            break

        start = int(start)
        end = int(end)

        if start > df.shape[0] - 1:
            client.send('Invalid request'.encode(FORMAT))

        data = df.loc[start:end]
        client.send(data.to_string().encode(FORMAT))

    client.close()


def start():
    # Listen for connections
    server.listen()
    print('[SERVER] Listening on:', ADDR)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=serve_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')


print('[SERVER] Starting...')
start()
