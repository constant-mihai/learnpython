#!/usr/bin/python3

lookahead = 0

#
# Match
#
def match(expression, char):
    global lookahead
    print ("Pos = {}, Lookahead = {}".format(lookahead, expression[lookahead]))
    if expression[lookahead] == char:
           lookahead+=1
    else:
        raise Exception("Error matching: {}".format(char))

#
#  Parse expression
#
def parse_expression_1(expression):
    """
    Dragon book excercise 2.4.1. c)
    Third expression: S -> 0 S 1 | 0 1
    The production is ambigous for a predictive parser . It brakes the rule saying
    that First(prod_1) must be disjoint from First(prod2)

    My first solution is to just parse it wrong (potentially) and then right a 
    second time.
    """
    global lookahead
    if len(expression) <= lookahead:
        print("Parsed everything.")
        return
    print ("Lookahead = {}".format(lookahead))
    if expression[lookahead] == "0":
        match(expression, "0")
        # Try the first case 0 S 1
        parse_expression_1(expression)
        match(expression, "1")
    elif expression[lookahead] == "1":
        # S expressions always start with a "0" 
        # go back and try parsing for the other production
        return
    else:
        print("Char: " + expression[lookahead])


#
# Parse expression
#
def parse_expression_2(expression):
    """
    A second option is to do this: \
    https://github.com/fool2fish/dragon-book-exercise-answers/blob/master/ch02/2.4/2.4.1.3.c

    In short:
    S -> 0 S 1 | 0 1
    -----------------
    S -> 0 R
    R -> S 1 | 1
    """
    global lookahead
    if len(expression) <= lookahead:
        print("Parsed everything.")
        return
    if expression[lookahead] == "0":
        match(expression, "0")
        parse_expression_R(expression)
    else:
        print("Char: " + expression[lookahead])

#
#  Parse expression
#
def parse_expression_R(expression):
    if expression[lookahead] == "1":
        match(expression, "1")
    else:
        parse_expression_2(expression)
        match(expression, "1")

#
# Main
#
def main():
    print("Introduce an expresion of the type: ")
    print("S -> 0 S 1 | 0 1 ")
    print("No spaces.")
    expression = input("Input:")

    lookahead = 0
    parse_expression_2(expression)


#
# Module check
#
if __name__ == "__main__":
    main()
