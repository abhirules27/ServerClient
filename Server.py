# Server Code 1: On Attackers Machine (new)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ATTACKER_OWN_IP = '192.168.0.199'
PORT = 1234
s.bind((ATTACKER_OWN_IP, PORT))



s.listen()
print("Listening...")
while True:
    clientsocket, address = s.accept()
    print(f'Connection from {address} established!')
    clientsocket.send(bytes("Welcome message from Server", "utf-8"))
    clientsocket.close()