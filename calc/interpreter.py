#!/usr/bin/python3
import pdb
import logger 
import calc_lexeme as lxm 
import calc_token as tkn 
import ast

log = logger.create_logger("Interpreter")
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
        log.warning("Ordered {}".format(token_type))
        log.warning("Got {}:{}".format(self.__lexeme.token().type, \
                self.__lexeme.token().value))
        if self.__lexeme.token().type == token_type:
            self.__lexeme.next_token()
        else:
            self.indigestion(token_type, self.__lexeme.token().type)

    #
    # Program
    #
    def program(self):
        log.warning("IN:")
        """program : compound_statement DOT"""

        self.eat(tkn.Type.PROGRAM)
        variable_node = self.variable()
        program_name = variable_node.value

        self.eat(tkn.Type.SEMI)

        block_node = self.block()
        program_node = ast.Program(program_name, block_node)

        self.eat(tkn.Type.DOT)

        return program_node

    #
    # Block
    #
    def block(self):
        log.warning("IN:")
        declaration_nodes = self.declarations()
        compound_statement_nodes = self.compound_statement()
        block_node = ast.Block(declaration_nodes, compound_statement_nodes)
        return block_node 

    #
    # Declarations
    #
    def declarations(self):
        log.warning("IN:")
        """declarations : VAR (variable_declaration SEMI)+
                    | (PROCEDURE ID SEMI block SEMI)*
                    | empty
        """
        declarations = []
        if self.__lexeme.token().type == tkn.Type.VAR:
            self.eat(tkn.Type.VAR)
            while self.__lexeme.token().type == tkn.Type.ID:
                var_decl = self.variable_declaration()
                declarations.extend(var_decl)
                self.eat(tkn.Type.SEMI)

        while self.__lexeme.token().type == tkn.Type.PROCEDURE:
            self.eat(tkn.Type.PROCEDURE)
            proc_name = self.__lexeme.token().value
            self.eat(tkn.Type.ID)
            self.eat(tkn.Type.SEMI)
            block_node = self.block()
            proc_decl = ast.ProcedureDecl(proc_name, block_node)
            declarations.append(proc_decl)
            self.eat(tkn.Type.SEMI)

        return declarations

    #
    # Variable declaration
    #
    def variable_declaration(self):
        log.warning("IN:")
        """variable_declaration : ID (COMMA ID)* COLON type_spec"""
        var_nodes = [ast.Var(self.__lexeme.token())]  # first ID
        self.eat(tkn.Type.ID)

        while self.__lexeme.token().type == tkn.Type.COMMA:
            self.eat(tkn.Type.COMMA)
            var_nodes.append(ast.Var(self.__lexeme.token()))
            self.eat(tkn.Type.ID)

        self.eat(tkn.Type.COLON)

        type_node = self.type_spec()
        var_declarations = [
            ast.VarDecl(var_node, type_node)
            for var_node in var_nodes
        ]
        return var_declarations

    ##
    # Type spec
    #
    def type_spec(self):
        log.warning("IN:")
        """type_spec : INTEGER
                     | REAL
        """
        token = self.__lexeme.token()
        if self.__lexeme.token().type == tkn.Type.INTEGER:
            self.eat(tkn.Type.INTEGER)
        else:
            self.eat(tkn.Type.REAL)
        node = ast.Type(token)
        return node

    #
    # Compound statement
    #
    def compound_statement(self):
        log.warning("IN:")
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
        log.warning("IN:")
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
        log.warning("IN:")
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
        log.warning("IN:")
        """
        assignment_statement : variable ASSIGN expr
        """
        left = self.variable()
        token = self.__lexeme.token()
        self.eat(tkn.Type.ASSIGN)
        right = self.expr()
        node = ast.Assign(left, token, right)
        return node

    #
    # Variable
    #
    def variable(self):
        log.warning("IN:")
        """
        variable : ID
        """
        node = ast.Var(self.__lexeme.token())
        self.eat(tkn.Type.ID)
        return node

    #
    # Empty
    #
    def empty(self):
        log.warning("IN:")
        """An empty production"""
        return ast.NoOp()

    #
    # Factor
    #
    def factor(self):
        log.warning("IN:")
        """
        factor : PLUS factor
              | MINUS factor
              | INTEGER_CONST
              | REAL_CONST
              | LPAREN expr RPAREN
              | variable

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
        elif self.__lexeme.token().type == tkn.Type.INTEGER_CONST:
            node = ast.Num(self.__lexeme.token())
            self.eat(tkn.Type.INTEGER_CONST)
        elif self.__lexeme.token().type == tkn.Type.REAL_CONST:
            node = ast.Num(self.__lexeme.token())
            self.eat(tkn.Type.REAL_CONST)
        else :
            node = self.variable()

        return node 

    #
    # Term
    #
    def term(self):
        log.warning("IN")
        """
        term : factor ((MUL | DIV | FLOAT_DIV) factor)*
        """
        node = self.factor()

        while self.__lexeme.token().type in (tkn.Type.MUL, tkn.Type.DIV, tkn.Type.FLOAT_DIV):
            token = self.__lexeme.token()
            if token.type == tkn.Type.MUL:
                self.eat(tkn.Type.MUL)
            elif token.type == tkn.Type.DIV:
                self.eat(tkn.Type.DIV)
            elif token.type == tkn.Type.FLOAT_DIV:
                self.eat(tkn.Type.FLOAT_DIV)

            node = ast.BinOp(left=node, op=token, right=self.factor())

        return node 

    #
    # Expr
    #
    def expr(self):
        log.warning("IN")
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
