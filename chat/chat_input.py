#!/usr/bin/python3

#
# Reads input
#
class Chat_input(object):
    #
    # Ctor
    #
    def __init__(self, queue):
        self.__q = queue

    #
    # Print the queue
    #
    def print_queue(self):
        for el in list(self.__q.queue):
            print(el)

    #
    # Get the input
    #
    def get_input(self):
        while True:
            try:
                text = input('chat> ')
                self.__q.put(text)
                #self.print_queue()
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
