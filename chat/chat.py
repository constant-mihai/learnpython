#!/usr/bin/python3
import chat_socket as chaso
import chat_input as chain
import message_processing as mespro 
import queue
import threading

#
# Main
#
def main():
    # Messages queue
    egress_queue = queue.Queue()
    client_cmd_q = queue.Queue()
    server_cmd_q = queue.Queue()

    # Message processor
    mp = mespro.Message_processing()

    # Start listener thread
    server_thread = chaso.Server(None, 50007, 
                                 server_cmd_q, 
                                 mp)
    server_thread.start()

    # Create client thread
    client_thread = chaso.Client("127.0.0.1", 50007,
                                 egress_queue, 
                                 client_cmd_q, 
                                 mp)
    # Start asking for input
    chat_input = chain.Chat_input(egress_queue, 
                                  client_cmd_q,
                                  server_cmd_q,
                                  client_thread)
    chat_input.get_input()

#
# Module check
#
if __name__ == "__main__":
    main()
