#!/usr/bin/python3
import logging
import calc_token as tkn 

logging.basicConfig(level=logging.WARNING,
        format='%(name)s:%(levelname)s\t'\
                '%(funcName)s():%(lineno)s\t' \
                '%(message)s')

#
# Parser Exception
#
class Parsing_error(Exception):
    #
    # Ctor
    #
    def __init__(self, text):
        print("Unkown char: {}".format(text))


#
# Lexeme class
#
class Lexeme():
    """
    program : compound_statement DOT

    compound_statement : BEGIN statement_list END

    statement_list : statement
                   | statement SEMI statement_list

    statement : compound_statement
              | assignment_statement
              | empty

    assignment_statement : variable ASSIGN expr

    empty :

    expr: term ((PLUS | MINUS) term)*

    term: factor ((MUL | DIV) factor)*

    factor : PLUS factor
           | MINUS factor
           | INTEGER
           | LPAREN expr RPAREN
           | variable

    variable: ID
    """

    #
    # Ctor
    #
    def __init__(self, text):
        """
        TODO rename to Lexer?
        WARNING !!! WARNING !!! WARNING!!!
        Anything in this class can advance __pos.
        WARNING !!! WARNING !!! WARNING!!!

        param[in] text      input  text
        """
        self.__words = dict()
        self.__words = {
                "BEGIN": tkn.Token(tkn.Type.BEGIN, "BEGIN"),
                "END": tkn.Token(tkn.Type.END, "END")
                }
        print(self.__words)
        # Object keeping position and current char
        self.__pos = tkn.Position(text)
        # The current token
        self.__token = None
        # Advance to the first token
        self.next_token() 
        # Keywords

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
    # Build a word (identifier)
    #
    def word(self):
        logging.warning("IN")
        result = ""
        while self.__pos.the_end() != True and \
              self.__pos.char().isalpha():
              
            result += self.__pos.char()
            self.__pos.adv(1)

        logging.warning("Word: {}".format(result))
        return result

    #
    # Builds an integer
    # TODO -- not tested
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
    # Map words
    #
    def map_words(self):
        s = self.word()
        if self.__words.get(s) is not None:
            return self.__words[s]
        else:
            self.__words[s] = tkn.Token(tkn.Type.ID, s) 
            return self.__words[s]


        
    #
    # White spaces
    # TODO -- not tested
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

            # self.peek() = self.text[self.__pos + i]
            # if self.peek().isspace() or \
               # self.peek().istab():#TODO
                # pass
            # elif self.peek().isnewline():#TODO
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

        if self.__pos.char().isalpha():
            self.__token = self.map_words()
            return

        if self.__pos.char() == ':' and self.peek() == '=':
            self.__token = tkn.Token(tkn.Type.ASSIGN, ':=')
            self.__pos.adv(1)
            self.__pos.adv(1)
            return 

        if self.__pos.char() == ';':
            self.__token = tkn.Token(tkn.Type.SEMI, ';')
            self.__pos.adv(1)
            return 

        if self.__pos.char() == '.':
            self.__token = tkn.Token(tkn.Type.DOT, '.')
            self.__pos.adv(1)
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

        if self.__pos.char()  == '(':
            self.__token = tkn.Token(tkn.Type.LPARAN, self.__pos.char())
            self.__pos.adv(1)
            return 
        if self.__pos.char()  == ')':
            self.__token = tkn.Token(tkn.Type.RPARAN, self.__pos.char())
            self.__pos.adv(1)
            return 
        
        # Reaching here means the char is not known
        raise Parsing_error(self.__pos.char())
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
