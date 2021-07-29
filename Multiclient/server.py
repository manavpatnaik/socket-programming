import socket
import threading

PORT = 1234
SERVER = socket.gethostname()
ADDR = (SERVER, PORT)
DISCONNECT = '!DISCONNECT'
CHUNK_SIZE = 32
FORMAT = 'utf-8'

# Init socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address
server.bind(ADDR)

# Method to handle a client connection
def handle_client(conn, addr):
    connected = True
    while connected:
        # Continually receive and print messages from clients
        msg = conn.recv(CHUNK_SIZE).decode(FORMAT)
        if len(msg) > 0:
            # Disconnect if the message is the DISCONNECT string
            if msg == DISCONNECT:
                connected = False
            print(f'[{addr}]: {msg}')

    conn.close()

def start():
    # Listen for connections
    server.listen()
    print('[SERVER] Listening on:', ADDR)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

print('[SERVER] Starting...')
start()