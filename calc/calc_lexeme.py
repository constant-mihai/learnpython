#!/usr/bin/python3
import logging
import calc_token as tkn 

logging.basicConfig(level=logging.WARNING,
        format='%(name)s:%(levelname)s\t'\
                '%(funcName)s():%(lineno)s\t' \
                '%(message)s')

#
# Lexeme class
#
class Lexeme():
    #
    # Ctor
    #
    def __init__(self, text):
        """
        TODO rename to Lexer?
        WARNING: Anything in this class can advance position.

        param[in] text      input  text
        """
        # Object keeping position and current char
        self.__pos = tkn.Position(text)
        # The current token
        self.__token = None
        # Advance to the first token
        self.next_token() 

    #
    # Error
    #
    def error(self):
        raise Exception('Error parsing input')

    #
    # Get token
    #
    def token(self):
        return self.__token

    #
    # Builds an integer
    #
    def integer(self):
        logging.warning("IN")
        result = ""
        while self.__pos.the_end() != True and \
              self.__pos.char().isdigit():
              
            result += self.__pos.char()
            self.__pos.adv(1)

        logging.warning("Integer: {}".format(result))
        return int(result)
        
    #
    # White spaces
    #
    def whitespaces():
        """
        Eats up the whitespaces, tabs and newlines.
        """
        i = 0 
        while True:
            i += 1
            
            if self.__pos.the_end():
                break

            # self.peek = self.text[self.__pos + i]
            # if self.peek.isspace() or \
               # self.peek.istab():#TODO
                # pass
            # elif self.peek.isnewline():#TODO
                # self.line += 1 
            # else: break

    #
    # Advances the token
    #
    def next_token(self):
        logging.warning("IN")
        """
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        if self.__pos.the_end():
            print("The End!")
            self.__token = tkn.Token(tkn.Type.EOF, None)
            return 

        while self.__pos.char().isspace():
            print("is space!")
            self.__pos.adv(1)

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.__pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if self.__pos.char().isdigit():
            num = int(self.integer())
            self.__token = tkn.Token(tkn.Type.INTEGER, num)
            return

        if self.__pos.char()  == '+':
            self.__token = tkn.Token(tkn.Type.PLUS, self.__pos.char())
            self.__pos.adv(1)
            return 

        if self.__pos.char()  == '-':
            self.__token = tkn.Token(tkn.Type.MINUS, self.__pos.char())
            self.__pos.adv(1)
            return 

        if self.__pos.char()  == '*':
            self.__token = tkn.Token(tkn.Type.MUL, self.__pos.char())
            self.__pos.adv(1)
            return 

        if self.__pos.char()  == '/':
            self.__token = tkn.Token(tkn.Type.DIV, self.__pos.char())
            self.__pos.adv(1)
            return 

        self.error()


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
