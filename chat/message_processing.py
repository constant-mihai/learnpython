#!/usr/bin/python3

import chat_messages as chame
import pickle


#
# Message processing
#
class Message_processing():
    #
    # Ctor
    #
    def __init__(self):
        self.__bye = False


    #
    # Process the message
    #
    def process(self, data):
        if data is None or \
                len(data) == 0:
            #print("Received empty buffer to process")
            return
        msg = pickle.loads(data) 
        if msg.type == chame.Type.HELLO:
            print("User {} says hello".format(msg.m_from))
        elif msg.type == chame.Type.BYE:
            print("User {} says bye".format(msg.m_from))
            print("Closing the connection.")
            self.__bye = True
            #s.shutdown(socket.SHUT_RDWR)
            #s.close()
        elif msg.type == chame.Type.TXT:
            print("User {} is saying: {}".format(
                                            msg.m_from,
                                            msg.value))

    #
    # 
    #
    def client_said_bye(self):
        return self.__bye

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
