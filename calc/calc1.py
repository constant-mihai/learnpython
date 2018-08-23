#!/usr/bin/python3
import sys
import symbol
import interpreter as intrpr
Interpreter = intrpr.Interpreter

#
# Command line
#
def command_line():
    text = ""
    line = ""
    while True:
        try:
            line = ""
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            line = input('calc> ')
            text += line
            text += "\n"
        except EOFError:
            break
        if not line:
            continue
        if "END." in line:
            print(text)
            interpreter = Interpreter(text)
            root = interpreter.program()
            result = interpreter.parse_tree(root)
            print(result)
            text = ""
            
#
# Parse file
#
def parse_file(name):
    f = open(name, "r")
    text = f.read()
    print(text)
    # Parse file 
    interpreter = Interpreter(text)
    root = interpreter.program()

    # Visit tree and Create symbol table
    symbol_builder = symbol.SymbolTableBuilder()
    symbol_builder.visit(root)

    # Visit tree again and interpret 
    result = interpreter.parse_tree(root)
    print(result)


#
# Main
#
def main():
    parse_file(sys.argv[1])

if __name__ == '__main__':
    main()
