#!/usr/bin/python3
import ast
import symbol

#
# Semantic analayzer
#
class SemanticAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.symtab = symbol.SymbolTable()

    def visit_Block(self, node):
        for declaration in node.declarations:
            self.visit(declaration)
        self.visit(node.compound_statement)

    def visit_Program(self, node):
        self.visit(node.block)

    def visit_Compound(self, node):
        for child in node.children:
            self.visit(child)

    def visit_NoOp(self, node):
        pass

    def visit_VarDecl(self, node):
        # For now, manually create a symbol for the INTEGER built-in type
        # and insert the type symbol in the symbol table.
        type_symbol = BuiltinTypeSymbol('INTEGER')
        self.symtab.insert(type_symbol)

        # We have all the information we need to create a variable symbol.
        # Create the symbol and insert it into the symbol table.
        var_name = node.var_node.value
        var_symbol = VarSymbol(var_name, type_symbol)
        self.symtab.insert(var_symbol)

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
