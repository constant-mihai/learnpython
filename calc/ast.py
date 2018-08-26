#!/usr/bin/python3
import logger 
import calc_token as tkn 

log = logger.create_logger("AST")

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
# Program
#
class Program(AST):
    def __init__(self, name, block):
        self.name = name
        self.block = block

#
# Block
#
class Block(AST):
    def __init__(self, declarations, compound_statement):
        self.declarations = declarations
        self.compound_statement = compound_statement

#
# Var decl
#
class VarDecl(AST):
    def __init__(self, var_node, type_node):
        self.var_node = var_node
        self.type_node = type_node

#
# Procedure
#
class ProcedureDecl(AST):
    def __init__(self, proc_name, block_node):
        self.proc_name = proc_name
        self.block_node = block_node

#
# Type
#
class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

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
# Num
#
class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

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
class NodeVisitor(object):
    #
    # Ctor
    #
    def __init__(self):
        self.GLOBAL_SCOPE = dict()

    #
    # Visit method
    #
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        log.warning("IN, : {}".format(type(node)))
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
        super().__init__()

    #
    # Visit program
    #
    def visit_Program(self, node):
        self.visit(node.block)

    #
    # Visit Block
    # 
    def visit_Block(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    #
    # Visit Var declaration
    #
    def visit_VarDecl(self, node):
        # Do nothing
        pass

    #
    # Visit Type
    #
    def visit_Type(self, node):
        # Do nothing
        pass

    #
    # Visit unary
    #
    def visit_UnaryOp(self, node):
        log.warning("IN, op: {}".format(node.op.type))
        if node.op.type == tkn.Type.PLUS:
            log.warning("Plus")
            return +self.visit(node.expr)
        elif node.op.type == tkn.Type.MINUS:
            log.warning("Minus")
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
        elif node.op.type == tkn.Type.FLOAT_DIV:
            print("/")
            return (left / right)
        elif node.op.type == tkn.Type.DIV:
            print("DIV")
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
    # Visit num 
    #
    def visit_Num(self, node):
        print(node.value)
        return node.value 

    #
    # Assign
    #
    def visit_Assign(self, node):
        var_name = node.left.value
        print(var_name)
        self.GLOBAL_SCOPE[var_name] = self.visit(node.right)
        print(self.GLOBAL_SCOPE)

    #
    # Visit var
    #
    def visit_Var(self, node):
        var_name = node.value
        val = self.GLOBAL_SCOPE.get(var_name)
        if val is None:
            raise NameError(repr(var_name))
        else:
            print(val)
            return val

    #
    # Visit procedure decl
    #
    def visit_ProcedureDecl(self, node):
        pass

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
