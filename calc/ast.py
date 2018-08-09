#!/usr/bin/python3
import calc_token as tkn 

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

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

#
# Specific node visitor
#
class CalcVisitor(NodeVisitor):
    def __init__(self):
        pass 

    def visit_BinOp(self, node):
        if node.op.type == tkn.Type.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == tkn.Type.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == tkn.Type.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == tkn.Type.DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Token(self, node):
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
