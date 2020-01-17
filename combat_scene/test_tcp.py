from socket import *
from random import randint

socket = socket()
socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ADDRESS = ('172.40.75.152', 8888)
socket.bind(ADDRESS)
socket.listen(3)

print('waiting for connection')
receiver, address = socket.accept()
while True:
    pos = str(randint(400, 600)) + ',' + str(randint(300, 500)) + '.'
    print('send pos', pos)
    receiver.send(pos.encode())
    data = receiver.recv(1024)