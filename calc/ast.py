#!/usr/bin/python3
import logging
import calc_token as tkn 

logging.basicConfig(level=logging.WARNING,
        format='%(name)s:%(levelname)s\t'\
                '%(funcName)s():%(lineno)s\t' \
                '%(message)s')


#
#  Abstract syntax tree
#
class AST():
    #
    # Ctor
    #
    def __init__(self):
        self.__root = None
        self.GLOBAL_SCOPE = dict()


#
# Node
#
class BinOp(AST):
    #
    # Ctor
    #
    def __init__(self, left, op, right):
        self.left = left  
        self.op = op 
        self.right = right

#
# Unary op
#
class UnaryOp(AST):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

#
# Compound
#
class Compound(AST):
    """Represents a 'BEGIN ... END' block"""
    def __init__(self):
        self.children = []

#
# Assign
#
class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        # Why op? TODO
        self.token = self.op = op
        self.right = right

#
# Var
#
class Var(AST):
    """The Var node is constructed out of ID token."""
    def __init__(self, token):
        self.token = token
        self.value = token.value

#
# NoOp
#
class NoOp(AST):
    pass

#
# Generic node visitor
# https://ruslanspivak.com/lsbasi-part7/
# https://docs.python.org/2.7/library/ast.html#module-ast
#
class NodeVisitor():
    #
    # Ctor
    #
    def __init__(self):
       pass 

    #
    # Visit method
    #
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    #
    # Raises exception on missing method
    #
    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

#
# Specific node visitor
#
class CalcVisitor(NodeVisitor):
    #
    # Ctor
    #
    def __init__(self):
        pass 

    #
    # Visit unary
    #
    def visit_UnaryOp(self, node):
        logging.warning("IN, op: {}".format(node.op.type))
        if node.op.type == tkn.Type.PLUS:
            logging.warning("Plus")
            return +self.visit(node.expr)
        elif node.op.type == tkn.Type.MINUS:
            logging.warning("Minus")
            return -self.visit(node.expr)

    #
    # Visit Bin op
    #
    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if node.op.type == tkn.Type.PLUS:
            print("+")
            return (left + right)
        elif node.op.type == tkn.Type.MINUS:
            print("-")
            return (left - right)
        elif node.op.type == tkn.Type.MUL:
            print("*")
            return (left * right)
        elif node.op.type == tkn.Type.DIV:
            print("/")
            return (left / right)

    #
    # Visit Token
    #
    def visit_Token(self, node):
        print(node.value)
        return node.value

    #
    # Visit compound
    #
    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    #
    # Visit no op
    #
    def visit_NoOp(self, node):
        pass

    #
    # Assign
    #
    def visit_Assign(self, node):
        var_name = node.left.value
        self.GLOBAL_SCOPE[var_name] = self.visit(node.right)

    #
    # Visit var
    #
    def visit_Var(self, node):
        var_name = node.value
        val = self.GLOBAL_SCOPE.get(var_name)
        if val is None:
            raise NameError(repr(var_name))
        else:
            return val

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
