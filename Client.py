# Client Codee

# To be converted in exe
import socket

SERVER_IP = '192.168.0.181'
SERVER_PORT = 5678

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    data = s.recv(1024)
    print(data)

input() // To
stay
on
Screen
