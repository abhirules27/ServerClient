# Server Code

# Learning Socket Module
import socket

SERVER_IP='192.168.0.200'
SERVER_PORT=5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    //AF_INET means IPv4. SOCK_STREAM means protocol TCP.
                                                                // For UDP, use SOCK_DGRAM
    s.bind((SERVER_IP,SERVER_PORT))
    print("Server Listening...")
    s.listen(1)                                                 // This will listen for One Connection
                                                                // This will stop code exec, till it gets Connection
    conn, addr = s.accept()
    print(f'Connection estb from: {addr}')

    with conn:
        while True:
            conn.send(b'Hello World!')
            break