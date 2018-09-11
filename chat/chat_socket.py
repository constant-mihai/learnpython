#!/usr/bin/python3

# Echo server program
import socket
import sys
import pdb
import threading
import prctl 
import time 
import chat_messages as chame
import pickle
import logger

#
# Server
#
class Server(threading.Thread):
    # #
    # Ctor
    #
    def __init__(self, host, port, cmd_q, mp):
        super(Server, self).__init__()
        self.__host = host
        self.__port = port 
        self.__cmd_q = cmd_q 
        self.__processor = mp 
        self.__log = logger.create_logger("Server", "server.log")


    #
    # Overload run
    #
    def run(self):
        s = None
        prctl.set_name("chat_server")
        #pdb.set_trace()
        for res in socket.getaddrinfo(self.__host, self.__port, socket.AF_UNSPEC,
                                      socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
            af, socktype, proto, canonname, sa = res
            try:
                s = socket.socket(af, socktype, proto)
            except OSError as msg:
                s = None
                continue
            try:
                s.bind(sa)
                s.listen(1)
            except OSError as msg:
                s.close()
                s = None
                continue
            break

        if s is None:
            print('could not open socket')
            sys.exit(1)

        # Accept
        #pdb.set_trace()
        conn, addr = s.accept()
        with conn:
            self.__log.warning('Connected by {}'.
                    format(addr))
            # TODO
            # If the connection is alive it will block on recv
            # Else it will put the cpu in 100% when the client dies
            # Check for connection and break when dead
            while True:
                data = conn.recv(1024)
                self.__processor.process(data)
                if self.__processor.client_said_bye():
                    print("Closing the Server.")
                    s.shutdown(socket.SHUT_RDWR)
                    s.close()
                    break
                #if data: print(data)
                #conn.send(data)


#
# Client
#
class Client(threading.Thread):
    #
    # Ctor
    #
    def __init__(self, host, port, input_q, cmd_q, mp):
        super(Client, self).__init__()
        self.__host = host
        self.__port = port 
        self.__input_q = input_q
        self.__cmd_q = cmd_q
        self.__processor = mp

    #
    # Send bye
    #
    def send_bye(self, socket):
        msg = chame.Message(0, 1,
                  chame.Type.BYE, 0, 0) 
        ser = pickle.dumps(msg)
        socket.sendall(ser)


    #
    # Starts the thread
    #
    def run(self):
        prctl.set_name("chat_client")
        s = None
        for res in socket.getaddrinfo(self.__host, self.__port, socket.AF_UNSPEC, socket.SOCK_STREAM):
            #pdb.set_trace()
            af, socktype, proto, canonname, sa = res
            try:
                s = socket.socket(af, socktype, proto)
            except OSError as error_msg:
                s = None
                continue
            try:
                print("Connect to {}.".format(sa))
                s.connect(sa)
            except OSError as error_msg:
                s.close()
                s = None
                print(error_msg)
                continue
            break
        if s is None:
            print('could not open socket')
            sys.exit(1)
        with s:
            msg = None
            while True:
                if self.__cmd_q.empty() == False:
                    cmd = self.__cmd_q.get()
                    if cmd == "exit":
                        print("Closing the connection.")
                        self.send_bye(s)
                        s.shutdown(socket.SHUT_RDWR)
                        s.close()
                        break
                if self.__input_q.empty() == False:
                    msg = self.__input_q.get()
                    s.sendall(msg)
                #data = s.recv(1024)
                #print('Received', repr(data))
                time.sleep(1)

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
