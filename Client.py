# Client Code:  Code 1
# To be converted in exe

# import socket
# SERVER_IP='192.168.0.199'
# SERVER_PORT=5678
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((socket.gethostname(), SERVER_PORT))
#     data = s.recv(1024)
#     print(data)
#
# input()                         #To stay on Screen
# _________________________________________________________________

# Client Code: Code 2 (On Victim's PC)

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")
print(full_msg)