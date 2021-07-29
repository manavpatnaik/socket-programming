import socket

PORT = 5001
SERVER = socket.gethostname()
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT = "DISCONNECT"
CHUNK_SIZE = 1024


# Create socket object and connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


# Method to send message to server
def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)


def recv(client):
    data = client.recv(CHUNK_SIZE).decode('utf-8')
    print(data)


while True:
    start = input('Start: ')
    send(start)
    if start == DISCONNECT:
        break

    end = input('End: ')
    send(end)
    if end == DISCONNECT:
        break
    recv(client)
