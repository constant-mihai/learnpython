#!/usr/bin/python3

import chat_messages as chame
import pickle
import logger 


#
# Message processing
#
class Message_processing():
    #
    # Ctor
    #
    def __init__(self):
        self.__bye = False
        self.__log = logger.create_logger("Message Processing", "main.log")


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
            self.__log.debug("User {} says hello".format(msg.m_from))
        elif msg.type == chame.Type.BYE:
            self.__log.debug("User {} says bye".format(msg.m_from))
            self.__log.debug("Closing the connection.")
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
