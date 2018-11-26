import time
import json

class Message:

    def __init__(self):
        self.__action = "presense"
        self.__time = time.ctime(time.time())

    def get_message(self):
        return {
            "action": self.__action,
            "time": self.__time,
        }

    def toJson(self):
        try:
           print(self.get_message())
        except Exception:
            print("Ошибка в конвертации в json")
