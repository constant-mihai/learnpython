#!/usr/bin/python3

# Echo server program
import socket
import sys
import pdb


class Server:
    def __init__(self, host, port):
        s = None
        #pdb.set_trace()
        for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC,
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
        pdb.set_trace()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            # TODO
            # If the connection is alive it will block on recv
            # Else it will put the cpu in 100% when the client dies
            # Check for connection and break when dead
            while True:
                data = conn.recv(1024)
                if data: print(data)
                conn.send(data)


class Client:
    def __init__(self, host, port):
        s = None
        for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
            #pdb.set_trace()
            af, socktype, proto, canonname, sa = res
            try:
                s = socket.socket(af, socktype, proto)
            except OSError as msg:
                s = None
                continue
            try:
                print("Connect to {}.".format(sa))
                s.connect(sa)
            except OSError as msg:
                s.close()
                s = None
                print(msg)
                continue
            break
        if s is None:
            print('could not open socket')
            sys.exit(1)
        with s:
            while True:
                try:
                    text = input('calc> ')
                    s.sendall(bytes(text, "ascii"))
                    data = s.recv(1024)
                    print('Received', repr(data))
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
