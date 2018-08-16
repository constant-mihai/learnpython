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


#
# Node
#
class BinOp():
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
# Main
#
def main():
    pass

#
# Module check
#
if __name__ == "__main__":
    main()
