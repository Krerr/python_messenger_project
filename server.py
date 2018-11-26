from socket import *
import sys
import json
from jim.response.response import Response
from jim.response.response_codes import Response_Code

class Jim_server:

    def __init__(self,  port=7777):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__port = port
        self.__socket.bind(("localhost", self.__port))
        self.__socket.listen(5)

    def start_handling(self):
        while True:
            response = Response()
            code = Response_Code()
            try:
                client, addr = self.__socket.accept()
                data = client.recv(1024 * 1024 * 5)
                print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом:', addr)
                client.send(json.dumps(response.get_response_ok(code.success["ok"], "Ok")).encode("utf-8"))
                client.close()
            except Exception:
                client.send(json.dumps(response.get_response_error(code.server_error["default_server_error"], "Server error")).encode("utf-8"))
                client.close()

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        server = Jim_server(int(sys.argv[1]))
    else:
        server = Jim_server()
    server.start_handling()