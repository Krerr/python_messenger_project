from jim.message.message import Message
import time


class Presence_Message(Message):

    def __init__(self, type = "status"):
        self.__action = "presense"
        self.__type = type
        self.__time = time.ctime(time.time())

    def get_message(self):
        return {
            "action": self.__action,
            "time": self.__time,
            "type": self.__type,
            "user": {
                "account_name": "John",
                "status": "Yep, I am here!"
            }
        }