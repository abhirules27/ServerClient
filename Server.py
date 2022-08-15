# # Server Code 1: On Attackers Machine
#
# # Learning Socket Module
# import socket
#
# SERVER_IP='192.168.0.200'
# SERVER_PORT=5678
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    //AF_INET means IPv4. SOCK_STREAM means protocol TCP.
#                                                                 // For UDP, use SOCK_DGRAM
#     s.bind((SERVER_IP,SERVER_PORT))
#     print("Server Listening...")
#     s.listen(1)                                                 // This will listen for One Connection
#                                                                 // This will stop code exec, till it gets Connection
#     conn, addr = s.accept()
#     print(f'Connection estb from: {addr}')
#
#     with conn:
#         while True:
#             conn.send(b'Hello World!')
#             break
# _______________________________________________________________

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen()

while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} established!')
    clientsocket.send(bytes("Welcome to Server", "utf-8"))
    clientsocket.close()