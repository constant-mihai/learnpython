#!/usr/bin/python3

from enum import Enum
import pickle
import chat_messages as chame

#
# Command types
#
class Type(Enum):
    EXIT = 0,
    CHAT_UP = 1,

#
# Command class
#
class Command(object):
    #
    # Ctor
    #
    def __init__(self, chat_input, client_cmd_q):
        self.__chat_input = chat_input
        self.__client_cmd_q = client_cmd_q 

    #
    # Interpret the given command
    #
    def interpret(self, command):
        # Just print the command for now
        print("This is the command '{}'".format(command))
        if len(command) == 0:
            return
        elif command[0] == ":":
            cmd = command[1:]
        else:
            cmd = command
        print("This is the cmd '{}'".format(cmd))

        # TODO hardcoded
        uid_client = 0
        uid_server = 1

        if cmd == "exit":
            msg = chame.Message(uid_client, uid_server,
                                chame.Type.BYE, 0, 0) 
            ser = pickle.dumps(msg)
            self.__chat_input.get_q().put(ser)
            self.__client_cmd_q.put(cmd)
            self.__chat_input.set_in_chat(False)
        elif cmd == "chat":
            self.__chat_input.set_in_chat(True)
            # Start client thread here
            msg = chame.Message(uid_client, uid_server, 
                                chame.Type.HELLO,
                                0, 0)
            ser = pickle.dumps(msg)
            self.__chat_input.get_q().put(ser)
            self.__chat_input.start_client_thread()



#
# Main
#
def main():
    pass

#
# Module check
#
if __name__ == "__main__":
    main()
