#!/usr/bin/python3
import first as fir
from enum import Enum 

#
# Production types
#
class Production_type:
    aBb, aB, large = 0, 1, 2

#
# Check production follow
#
def check_production(A, follow_set, first_set, productions, parent = None):
    production_data_structure = productions[A]
    print("Follow for: ", A, ":", production_data_structure)

    X = production_data_structure[2]
    i, j = 0, 0 
    # Go through the list of productions (str)
    while i < len(X):
        j = 0
        production_string = X[i]
        print("\tProd Str:", production_string)

        # Get the production type. Depending on the type create the follow_set set.
        prod_type, B, b = get_production_type(production_string, productions)
        if prod_type == Production_type.aBb:
            print("\tUpdating follow_set[" + B + "] with first_set[" +
                    b + "]")
            b_set = fir.get_first_set(b, first_set)
            follow_set[B]["terminals"].update(b_set - set("@"))
            if "@" in b_set:
                follow_set[B]["terminals"].update(follow_set[A]["terminals"])
        elif prod_type == Production_type.aB:
            print("\tUpdating follow_set[" + B + "] with follow_set[" +
                    A + "]")
            follow_set[B]["terminals"].update(follow_set[A]["terminals"])
        elif prod_type == Production_type.large:
            print("\tProduction string is to large. Need to reduce it.")
            parse_large_production(production_string, follow_set, first_set, A, productions)

        else:
            print("\tProduction_type was not recognized. Possibly only terminals.")

        while j < len(production_string):        # Go through the string
            j+=1

        i+=1

#
# Check if production has epsilon 
#
def check_for_epsilon(prod, productions):
    # TODO add case for when prod is compound
    if fir.is_terminal(prod):
        if fir.is_epsilon(prod):
            return True 
        else: 
            return False
    else:
        # The production string is not a terminal
        return compound_can_be_epsilon(prod, productions)

#
# Check a compound for epsilons
#
def compound_can_be_epsilon(compound, productions):
    """
     If all NonTerminals have an epsilon production, then the compound
     can be epsilon.

     @param[compound] a compound production, e.g: ABC.

     @return true if it can be reduced to epsilon. All have epsilon.
             false if at most lacks epsilon.
     @return the NonTerminal up to which it can be reduced. E.g:
             if A contains epsilon and B contains epsilon, but C does not, then:
             return (false, C)
    """
    has_epsilon = False
    for X_i in compound:
        has_epsilon = False
        # alternatively can just:
        # has_epsilon = productions[X_i][1]

        for Y_k in productions[X_i][2]:
            if fir.is_epsilon(Y_k):
                has_epsilon = True
                break
        # Found a NonTerminal which does not have epsilon as production
        if has_epsilon is False: break;

    return has_epsilon, X_i 

#
# Parse a large production rule
#
def parse_large_production(production_string, follow_set, first_set, A, productions):
    """
    For a complex production, , we need to break it down to multiple
    productions of the forms: aB or aBb
    E.g. bLST:
    1. a = bLS, B = T

    E.g.: bLSTer
    1. a = bLS, B = T, b = er;      Follow(T) = First(er) = e
    2. a = bL,  B = S, b = Ter;     Follow(S) = First(Ter) = First(T)
    3. a = b,   B = L, b = STer;    Follow(L) = First(STer) = First(ST)

    In essence there will be an index moving back from the end of the string,
    iterating over NonTerminals. Each NonTerminal will represent the sandwiched
    B when it's turn comes up.

    @param[in]      production_string
    @param[in/out]  follow_set
    """
    k = len(production_string) - 1  # Last char in the string
    # Find the first non-terminal.
    while k > 0: # Greater than one since Bb is not a vaid form 
        B = production_string[k]
        b = production_string[k+1:]
        if fir.is_terminal(B) is True:
            k-=1
            continue

        # The aB case. The last character is a terminal
        if b == "" or\
           check_for_epsilon(b, productions) is True: 
            print("\t\tUpdating follow_set[" + B + "] with follow_set[" +
                    A + "]")
            follow_set[B]["terminals"].update(follow_set[A]["terminals"])
        else:
        # The aBb case. 
            print("\t\tUpdating follow_set[" + B + "] with first_set[" +
                    b + "]")
            b_set = fir.get_first_set(b, first_set)
            follow_set[B]["terminals"].update(b_set - set("@"))
            if "@" in b_set:
                follow_set[B]["terminals"].update(follow_set[A]["terminals"])
            
        k-=1

    if k == 0:
        print("\tOnly terminals, nothing to do.")

#
# Get production type
#
def get_production_type(string, productions):
    """
    Takes a production string and parses it in order to find the production rule
    type.

    @param[in] string

    @return production type {aB, aBb, large, None}
    """
    prod_type = None
    B = None
    b = None

    str_len= len(string)
    if str_len== 0:
        raise Exception("Production string cannot be 0.")
    elif str_len== 1:
        print("\t\t" + string + ": is self standing")
        prod_type = None
        B = None
        b = None
    elif str_len== 2:
        if fir.is_terminal(string[0]) != True and fir.is_terminal(string[1]):
            print("\t\t" + string + ": is Ab")
            prod_type = None
            B = None
            b = None
        elif fir.is_terminal(string[0]) and fir.is_terminal(string[1]):
            print("\t\t" + string + ": is ab")
            prod_type = None
            B = None
            b = None
        else:
            print("\t\t" + string + ": is aB")
            prod_type = Production_type.aB
            B = string[1] 
            b = None
    elif str_len == 3:
        # aBb, the character in the middle has to be non-terminal
        if fir.is_terminal(string[1]) != True:
            if check_for_epsilon(string[2], productions) is True:
                print("\t\t" + string + ": is aBbeps")
                print("\t\t" + string[2] + ": Has epsilon")
                prod_type = Production_type.aB
                B = string[1] 
                b = None 
            else:
                print("\t\t" + string + ": is aBb")
                prod_type = Production_type.aBb
                B = string[1] 
                b = string[2]
        elif fir.is_terminal(string[2]) != True:
            print("\t\t" + string + ": is abB, reduced to aB")
            prod_type = Production_type.aB
            B = string[2] 
            b = None
        else:
            print("\t\t" + string + ": is abc")
            prod_type = None 
            B = None 
            b = None

    elif str_len > 3:
        print("\t\t" + string + ": is 3+ char")
        prod_type = Production_type.large
        B = None 
        b = None

    return prod_type, B, b

#
# Calculates the current length of the follow set
#
def follow_set_len(follow_set):
    ret = 0
    for x_i in follow_set:
        ret += len(follow_set[x_i]["terminals"])

    return ret

#
# Calculates the follow sets
#
def follow(productions):
    """
    1. First put $ (the end of input marker) in Follow(S) (S is the start symbol)
    2. If there is a production A → aBb, (where a can be a whole string) then
       everything in FIRST(b) except for ε is placed in FOLLOW(B).
    3. If there is a production A → aB, then everything in FOLLOW(A) is in
       FOLLOW(B) 
    4. If there is a production A → aBb, where FIRST(b) contains ε,
       then everything in FOLLOW(A) is in FOLLOW(B)

    @param productions = {
            "X1" : [has_been_checked, has_epsilon, ["X2X3", "terminals"]],
            "X2" : [has_been_checked, has_epsilon, ["de", "@"]],
            "X3" : [has_been_checked, has_epsilon, ["fg"]],
            .
            .
            "Xk" : [has_been_checked, has_epsilon, ["z"]]
    }
 
    @return follow = { 
            "X1" : {
                "terminals" : [], <---- "$dft" 
                "compounds" : []  <---- "X2X3"
            }

            "X2" : {
                "terminals" : [], <---- "d@" 
                "compounds" : []  <---- ""
            }
    }
    """
    follow_set = {}
    first_set = fir.calculate_first_set(productions)

    i = 0

    
    for key in productions:
        # Create the follow_set set
        if key not in follow_set :
            follow_set[key] = {
                    "terminals" : set(),
                    "compounds" : set()
            }
        if i == 0: # stop after the first key
            follow_set[key] = {
                    "terminals" : set("$"),
                    "compounds" : set()
            }
        i+=1


    last_len = 0 
    curr_len = follow_set_len(follow_set)
    while curr_len > last_len:
        last_len = curr_len 
        for key in productions:
            # Put $ in Follow(S)
            check_production(key, follow_set, first_set, productions)
        curr_len = follow_set_len(follow_set)

    print(follow_set)


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
