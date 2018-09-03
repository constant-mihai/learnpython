#!/usr/bin/python3

# Echo server program
import socket
import sys
import pdb
import threading
import prctl 
import queue


#
# Server
#
class Server(threading.Thread):
    #
    # Ctor
    #
    def __init__(self, host, port, queue):
        super(Server, self).__init__()
        self.__host = host
        self.__port = port 
        self.__queue = queue 

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
            print('Connected by', addr)
            # TODO
            # If the connection is alive it will block on recv
            # Else it will put the cpu in 100% when the client dies
            # Check for connection and break when dead
            while True:
                data = conn.recv(1024)
                if data == b"EOT":
                    print("Closing the Server.")
                    s.shutdown(socket.SHUT_RDWR)
                    s.close()
                    break
                if data: print(data)
                conn.send(data)


class Client(threading.Thread):
    def __init__(self, host, port, queue):
        super(Client, self).__init__()
        self.__host = host
        self.__port = port 
        self.__queue = queue 


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
                if self.__queue.empty() != False:
                    msg = self.__queue.get()
                    s.sendall(bytes(msg, "ascii"))
                    if msg == "EOT":
                        print("Closing the connection.")
                        s.shutdown(socket.SHUT_RDWR)
                        s.close()
                        break
                data = s.recv(1024)
                print('Received', repr(data))

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
