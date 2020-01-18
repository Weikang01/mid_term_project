from socket import *

socket = socket()
ADDRESS = ('172.40.75.152', 8888)
socket.connect(ADDRESS)


def cur_position():
    return data


while True:
    data = socket.recv(1024).decode().strip('.').strip(',')
    cur_position()
    socket.send('ok'.encode())
