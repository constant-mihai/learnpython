#!/usr/bin/python3
#import pdb
import logging
import calc_lexeme as lxm 
import calc_token as tkn 
import ast

logging.basicConfig(level=logging.WARNING,
        format='%(name)s:%(levelname)s\t'\
                '%(funcName)s():%(lineno)s\t' \
                '%(message)s')

#
# Main
#
def main():
    pass

#
# Interpreter
#
class Interpreter(object):
    # 
    # Ctor
    #
    def __init__(self, text):
        """
        @param[in] text     is the input text
        """
        self.__lexeme = lxm.Lexeme(text)

    #
    # Error
    #
    def indigestion(self, expected, actual):
        raise Exception('Was expecting token type: {}' \
                ', instead received: {}'.format(expected, actual))

    #
    # Nom nom nom
    #
    def eat(self, token_type):
        """
        Eat the specified token_type.
        Raise exception if the lookahead is an unexpected token_type

         @param[in] token_type
        """
        logging.warning("Ordered {}".format(token_type))
        logging.warning("Got {}:{}".format(self.__lexeme.token().type, \
                self.__lexeme.token().value))
        if self.__lexeme.token().type == token_type:
            self.__lexeme.next_token()
        else:
            self.indigestion(token_type, self.__lexeme.token().type)

    #
    # Factor
    #
    def factor(self):
        logging.warning("IN:")
        """
        factor : INTEGER
        The factor is the smallest posible production
        the parser expects a string of digits here,
        anything else should raise an exception
        """
        # TODO, don't like the hidden (global) lookahead token
        if self.__lexeme.token().type == tkn.Type.LPARAN:
            self.eat(tkn.Type.LPARAN)
            ret = self.expr()
            self.eat(tkn.Type.RPARAN)

        else :
            ret = self.__lexeme.token().value
            self.eat(tkn.Type.INTEGER)

        return ret 

    #
    # Term
    #
    def term(self):
        logging.warning("IN")
        """
        term : factor ((MUL | DIV) factor)*
        """
        result = self.factor()

        while self.__lexeme.token().type in (tkn.Type.MUL, tkn.Type.DIV):
            token = self.__lexeme.token()
            if token.type == tkn.Type.MUL:
                self.eat(tkn.Type.MUL)
                result = result * self.factor()
            elif token.type == tkn.Type.DIV:
                self.eat(tkn.Type.DIV)
                result = result / self.factor()

        return result

    #
    # Expr
    #
    def expr(self):
        logging.warning("IN")
        """Arithmetic expression parser / interpreter.

        calc>  14 + 2 * 3 - 6 / 2
        17

        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER
        """
        result = self.term()

        while self.__lexeme.token().type in (tkn.Type.PLUS, tkn.Type.MINUS):
            token = self.__lexeme.token()
            if token.type == tkn.Type.PLUS:
                self.eat(tkn.Type.PLUS)
                result = result + self.term()
            elif token.type == tkn.Type.MINUS:
                self.eat(tkn.Type.MINUS)
                result = result - self.term()

        return result


#
# Module check
#
if __name__ == "__main__":
    main()
