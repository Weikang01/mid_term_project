from socket import *

socket = socket()
ADDRESS = ('172.40.75.152', 8888)
socket.connect(ADDRESS)

while True:
    data = socket.recv(1024).decode().strip('.').strip(',')
    print(data)
    socket.send('ok'.encode())