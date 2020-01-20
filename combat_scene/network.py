from socket import *


class Network:

    def __init__(self):
        self.client = socket()
        self.host = 'localhost'
        self.port = 8888
        self.addr = (self.host, self.port)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(128).decode()

    def send(self, data):
        try:
            reply = self.client.send(str.encode(data))
            return reply
        except error as e:  # return socket.error
            return str(e)
