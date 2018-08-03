#!/usr/bin/python3

lookahead = 0

#
# Match
#
def match(expression, char):
    global lookahead
    if expression[lookahead] == char:
           lookahead+=1
    else:
        raise Exception("Error matching: " + char)

#
#  Parse expression
#
def parse_expression(expression):
    parse_expression_R(expression)

#
#  Parse expression
#
def parse_expression_R(expression):
    """
    Dragon book excercise 2.4.1
    Second expression: S -> S (S) S | @
    The production is left recursive. Need to transform it to
    right recursive":
        A -> Aa | b
        -----------
        A -> bR
        R -> aR | @
    Derived into:
    S -> @R
    R -> (S) S R
    """
    global lookahead
    if len(expression) <= lookahead:
        print("Parsed everything.")
        return
    print ("Lookahead = {}".format(lookahead))
    if expression[lookahead] == "(":
        match(expression, "(")
        parse_expression_2(expression)
        match(expression, ")")
        parse_expression_2(expression)
        parse_expression_R(expression)
    else:
        print("Char: " + expression[lookahead])


#
# Main
#
def main():
    print("Introduce an expresion of the type: ")
    print("S -> S (S) S | @ ")
    print("No spaces.")
    expression = input("Input:")

    lookahead = 0
    parse_expression_2(expression)


#
# Module check
#
if __name__ == "__main__":
    main()
