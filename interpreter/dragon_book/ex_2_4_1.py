#!/usr/bin/python3

lookahead = 0

#
# Expression
#
def parse_expression(expression):
    """
    Dragon book excercise 2.4.1
    """
    global lookahead
    print ("Lookahead = {}".format(lookahead))
    if expression[lookahead] == "+":
        match(expression, "+")
        parse_expression(expression)
        parse_expression(expression)
    elif expression[lookahead] == "-":
        match(expression, "-")
        parse_expression(expression)
        parse_expression(expression)
    elif expression[lookahead] == "a":
        match(expression, "a")
    else:
        raise Exception("Syntax error! Char: " + expression[lookahead])

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
# Main
#
def main():
    global lookahead
    print("Introduce an expresion of the type: ")
    print("S -> + S S | - S S | a ")
    print("No spaces.")
    expression = input("Input:")

    parse_expression(expression)
    if len(expression) > lookahead:
        raise Exception("Exception when parsing. Extra characters:"
                "{} : {}".format(len(expression) - lookahead, expression[lookahead:]))


#
# Module check
#
if __name__ == "__main__":
    main()
