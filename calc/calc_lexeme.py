#!/usr/bin/python3
import pdb
import logger 
import calc_token as tkn 

log = logger.create_logger("Lexer")

#
# Parser Exception
#
class Parsing_error(Exception):
    #
    # Ctor
    #
    def __init__(self, text):
        log.exception("Unkown char: {}".format(text))


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
                "END": tkn.Token(tkn.Type.END, "END"),
                "PROGRAM": tkn.Token(tkn.Type.PROGRAM, "PROGRAM"),
                "DIV": tkn.Token(tkn.Type.DIV, "DIV"),
                'VAR': tkn.Token(tkn.Type.VAR, 'VAR'),
                'INTEGER': tkn.Token(tkn.Type.INTEGER, 'INTEGER'),
                'REAL': tkn.Token(tkn.Type.REAL, 'REAL'),
                'PROCEDURE': tkn.Token(tkn.Type.PROCEDURE, 'PROCEDURE'),
                }
        log.warning(self.__words)
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
        log.warning("IN")
        result = ""
        while self.__pos.the_end() != True and \
              ( self.__pos.char().isalpha() or \
                self.__pos.char().isdigit() ):
              
            result += self.__pos.char()
            self.__pos.adv(1)

        log.warning("Word: {}".format(result))
        return result

    #
    # Builds an integer
    # TODO -- float part not tested
    #
    def integer(self):
        log.warning("IN")
        result = ""
        while self.__pos.the_end() != True and \
              self.__pos.char().isdigit():
              
            result += self.__pos.char()
            self.__pos.adv(1)

        if self.__pos.char() == ".":
            result += self.__pos.char()
            self.__pos.adv(1)
            # parse the decimals
            while self.__pos.the_end() != True and \
                  self.__pos.char().isdigit():
                result += self.__pos.char()
                self.__pos.adv(1)
            log.warning("Float: {}".format(result))
            return False, float(result)
        else:
            log.warning("Integer: {}".format(result))
            return True, int(result)

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
    # Skip comments
    #
    def skip_comment(self):
        while self.__pos.char() != '}':
            self.__pos.adv(1)
        self.__pos.adv(1)  # the closing curly brace

        
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
        log.warning("IN")
        """
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        if self.__pos.the_end():
            log.warning("The End!")
            self.__token = tkn.Token(tkn.Type.EOF, None)
            return 

        while self.__pos.the_end() is not True:
            if self.__pos.char().isspace():
                log.warning("is space!")
                self.__pos.adv(1)

            elif self.__pos.char()  == '{':
                log.warning("is comment!")
                self.__pos.adv(1)
                self.skip_comment()

            else:
                break

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.__pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if self.__pos.char().isdigit():
            flag, num = self.integer()
            if flag is True:
                self.__token = tkn.Token(tkn.Type.INTEGER_CONST, num)
            else:
                self.__token = tkn.Token(tkn.Type.REAL_CONST, num)

            return

        if self.__pos.char().isalpha():
            self.__token = self.map_words()
            return

        if self.__pos.char() == ':' and self.__pos.peek() == '=':
            self.__token = tkn.Token(tkn.Type.ASSIGN, ':=')
            self.__pos.adv(1)
            self.__pos.adv(1)
            return 

        if self.__pos.char() == ':':
            self.__token = tkn.Token(tkn.Type.COLON, ':')
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

        if self.__pos.char() == ',':
            self.__token = tkn.Token(tkn.Type.COMMA, ',')
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
            self.__token = tkn.Token(tkn.Type.FLOAT_DIV, self.__pos.char())
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
        #raise Parsing_error(self.__pos.char())
        return
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
