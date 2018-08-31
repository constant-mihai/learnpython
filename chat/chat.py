#!/usr/bin/python3
import chat_socket as chaso

#
# Main
#
def main():
    server = chaso.Server(None, 50007)
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue

#
# Module check
#
if __name__ == "__main__":
    main()
