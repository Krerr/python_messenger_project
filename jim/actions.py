from enum import Enum

class Actions(Enum):

    authenticate = "authenticate"
    presence = "presence"
    quit = "quit"
    probe = "probe"

    msg = "msg"

    join = "join"
    leave = "leave"