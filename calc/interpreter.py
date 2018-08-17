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
        self.__visitor = ast.CalcVisitor()

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
    # Program
    #
    def program(self):
        logging.warning("IN:")
        """program : compound_statement DOT"""
        node = self.compound_statement()
        self.eat(tkn.Type.DOT)
        return node

    #
    # Compound statement
    #
    def compound_statement(self):
        logging.warning("IN:")
        """
        compound_statement: BEGIN statement_list END
        """
        self.eat(tkn.Type.BEGIN)
        nodes = self.statement_list()
        self.eat(tkn.Type.END)

        root = ast.Compound()
        for node in nodes:
            root.children.append(node)

        return root

    #
    # Statement list
    #
    def statement_list(self):
        logging.warning("IN:")
        """
        statement_list : statement
                       | statement SEMI statement_list
        """
        node = self.statement()

        results = [node]

        while self.__lexeme.token().type == tkn.Type.SEMI:
            self.eat(tkn.Type.SEMI)
            results.append(self.statement())

        if self.__lexeme.token().type == tkn.Type.ID:
            self.error()

        return results

    #
    # Statement
    #
    def statement(self):
        logging.warning("IN:")
        """
        statement : compound_statement
                  | assignment_statement
                  | empty
        """
        if self.__lexeme.token().type == tkn.Type.BEGIN:
            node = self.compound_statement()
        elif self.__lexeme.token().type == tkn.Type.ID:
            node = self.assignment_statement()
        else:
            node = self.empty()
        return node

    #
    # Assignment
    #
    def assignment_statement(self):
        logging.warning("IN:")
        """
        assignment_statement : variable ASSIGN expr
        """
        left = self.variable()
        token = self.__lexeme.token()
        self.eat(tkn.Type.ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    #
    # Variable
    #
    def variable(self):
        logging.warning("IN:")
        """
        variable : ID
        """
        node = Var(self.__lexeme.token())
        self.eat(tkn.Type.ID)
        return node

    #
    # Empty
    #
    def empty(self):
        logging.warning("IN:")
        """An empty production"""
        return ast.NoOp()

    #
    # Factor
    #
    def factor(self):
        logging.warning("IN:")
        """
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN

        The factor is the smallest posible production
        the parser expects a string of digits here,
        anything else should raise an exception
        """
        # TODO, don't like the hidden (global) lookahead token
        token = self.__lexeme.token()
        if self.__lexeme.token().type == tkn.Type.LPARAN:
            self.eat(tkn.Type.LPARAN)
            node = self.expr()
            self.eat(tkn.Type.RPARAN)
        elif self.__lexeme.token().type == tkn.Type.PLUS:
            self.eat(tkn.Type.PLUS)
            node = ast.UnaryOp(token, self.factor()) 
        elif self.__lexeme.token().type == tkn.Type.MINUS:
            self.eat(tkn.Type.MINUS)
            node = ast.UnaryOp(token, self.factor()) 
        else :
            node = self.__lexeme.token()
            self.eat(tkn.Type.INTEGER)

        return node 

    #
    # Term
    #
    def term(self):
        logging.warning("IN")
        """
        term : factor ((MUL | DIV) factor)*
        """
        node = self.factor()

        while self.__lexeme.token().type in (tkn.Type.MUL, tkn.Type.DIV):
            token = self.__lexeme.token()
            if token.type == tkn.Type.MUL:
                self.eat(tkn.Type.MUL)
            elif token.type == tkn.Type.DIV:
                self.eat(tkn.Type.DIV)

            node = ast.BinOp(left=node, op=token, right=self.factor())

        return node 

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
        node = self.term()

        while self.__lexeme.token().type in (tkn.Type.PLUS, tkn.Type.MINUS):
            token = self.__lexeme.token()
            if token.type == tkn.Type.PLUS:
                self.eat(tkn.Type.PLUS)
            elif token.type == tkn.Type.MINUS:
                self.eat(tkn.Type.MINUS)

            node = ast.BinOp(left=node, op=token, right=self.term())

        return node 

    #
    # Expr
    #
    def parse_tree(self, node):
        return self.__visitor.visit(node)


#
# Module check
#
if __name__ == "__main__":
    main()
