#!/usr/bin/python3
import chat_socket as chaso
import chat_input as chain
import queue
import threading

#
# Main
#
def main():
    # Messages queue
    input_queue = queue.Queue()

    # Start listener thread
    server_thread = chaso.Server(None, 50007, input_queue)
    server_thread.start()


    # Start client thread here
    client_thread = chaso.Client("127.0.0.1", 50007, input_queue)
    client_thread.start()

    # Start asking for input
    chat_input = chain.Chat_input(input_queue)
    chat_input.get_input()

#
# Module check
#
if __name__ == "__main__":
    main()
