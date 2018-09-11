#!/usr/bin/python3

import chat_commands as chaco
import pickle
import chat_messages as chame

#
# Reads input
#
class Chat_input(object):
    #
    # Ctor
    #
    def __init__(self, egress_queue, client_cmd_q, client_thread):
        self.__egress_q = egress_queue
        self.__client_cmd_q = client_cmd_q
        self.__in_chat = False
        self.__command = chaco.Command(self,
                self.__client_cmd_q)
        self.__peer = "localhost, hardcoded"
        self.__client_thread = client_thread 


    #
    # Get the input q
    #
    def get_q(self):
        return self.__egress_q

    #
    # Print the queue
    #
    def print_queue(self, raw):
        if raw:
            for el in list(self.__egress_q.queue):
                print(el)
        else:
            for el in list(self.__egress_q.queue):
                deser = pickle.loads(el)
                print(deser)

    #
    # Check if this is a command
    #
    def is_command(self, text):
        if len(text) == 0:
            return True
        if text[0] == ":":
            return True
        else:
            return False
        
    #
    # Set in chat
    #
    def set_in_chat(self, bool_val):
        self.__in_chat = bool_val

    #
    # Starth the client thread
    #
    def start_client_thread(self):
        self.__client_thread.start()

    #
    # Get the input
    #
    def get_input(self):
        while True:
            try:
                if self.__in_chat:
                    text = input("chatting {}> ".format(self.__peer))
                else:
                    text = input('chat command> ')
                # First check if this is a chat msg
                # or a command
                if self.__in_chat == True and\
                   self.is_command(text) == False:
                    # It's a chat message. Q-it for egress
                    msg = chame.Message(0, 1,
                                        chame.Type.TXT, len(text), text) 
                    ser = pickle.dumps(msg)
                    self.__egress_q.put(ser)
                else:
                    # It's a chat command. Interpret it.
                    self.__command.interpret(text)

                self.print_queue(False)
            except EOFError:
                break
            if not text:
                continue


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
