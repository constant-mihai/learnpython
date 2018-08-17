#!/usr/bin/python3
import interpreter as intrpr
Interpreter = intrpr.Interpreter

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        root = interpreter.program()
        result = interpreter.parse_tree(root)
        print(result)


if __name__ == '__main__':
    main()
