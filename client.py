from socket import *
import sys
import json
from jim.message.client_message import Presence_Message

class Jim_client:

    def __init__(self, addr='localhost', port=8888):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__addr = addr
        self.__port = port

    def connect(self):
        self.__socket.connect((self.__addr, self.__port))

    def new_message(self):
        presense = Presence_Message()
        self.__message = presense.get_message()

    def send_message(self):
        self.__socket.send(json.dumps(self.__message).encode('utf-8'))
        data = self.__socket.recv(1024*1024*5)
        print(data.decode('utf-8'))

    def close(self):
        self.__socket.close()


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        client = Jim_client(sys.argv[1], int(sys.argv[2]))
    else:
        client = Jim_client()
    client.connect()
    client.new_message()
    client.send_message()
    client.close()




