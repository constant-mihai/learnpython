#!/usr/bin/python3

#
# Check if it is terminal
#
def is_terminal(X):
    if X.isalpha() is not True:
        if X.isdigit():
            raise Exception("Digits cannot be part of production")
        else:
            return True
    else:
        return X.islower()

#
# Check if it is terminal
#
def is_epsilon(X):
    return X == "@"



#
# X is a production.
# need to go through it and check for firsts
#
def check_production(key, first, productions, parent = None):
    """
    For the production rule X -> X1 X2..Xk, go through all the production
    elements recursively. First(X): First(X1)
    If ε is in First(Xi) then check next production: First(Xi+1).

    @param[in]      X - a production
    @param[in/out]  first - the first set 
    """

    production_data_structure = productions[key]
    print("Checking for: ", key, ":", production_data_structure)
    has_epsilon = False 


    first[key] = {
            "terminals" : set(),
            "compounds" : set()
    }

    X = production_data_structure[2]
    i, j = 0, 0 
    # Go through the list of productions (str)
    while i < len(X):
        has_terminals = False 
        j = 0
        production_string = X[i]
        print("\tProd Str:", production_string)
        while j < len(production_string):        # Go through the string
            print("\t\tChecking ", production_string[j])
            if is_terminal(production_string[j]): 
                has_terminals = True
                if is_epsilon(production_string[j]):
                    has_epsilon = True
                    print("\t\tbingo")
                first[key]["terminals"].add(production_string[j])
                break
            else:
                first[key]["compounds"].add(production_string[j])
                if check_production(production_string[j], first, productions,
                                    first[key]["terminals"]) \
                is False: 
                    # Production doesn't have empty string
                    break               # we are done
                else:
                    # Production has an empty string
                    # We need to check next letter in the string.
                    # If it is a terminal we are done. Else it keeps checking.
                    # If all the Compounds in a row have an empty string and no
                    # terminals follow, reduce them to @. Means the rule above needs
                    # to treat the current Compund as if one of its productions
                    # was @.
                    # Example:
                    # H -> KLp
                    # K -> b | @
                    # L -> SK    <--- could be rewritten as: L -> b | d | db | @
                    # S -> d | @
                    # First(H): First(K), First(L), p -> b, d, _p_ (because of L)
                    # First(K): b, @
                    # First(L): First(S), First(K)
                    # First(S): d, @

                    # If we're at the end of a string of Compunds containing @
                    # and no terminals were found, then mark rule as containing @
                    if j == len(production_string) - 1:
                        if has_terminals is False:
                            has_epsilon = True;
                            first[key]["terminals"].add("@")
            j+=1
        i+=1
    print("----")

    if parent is not None:
        striped_sigma = first[key]["terminals"] - set("@")
        parent.update(striped_sigma)
        
    production_data_structure[0] = True # has been checked. Don't check it again
    production_data_structure[1] = has_epsilon 
    return has_epsilon 

#
# Get the first set for the given X
# 
def get_first_set(X, first_set):
    ret = set() 
    if is_terminal(X):
        ret.update(set(X[0]))
    else:
        if len(X) > 1:
            for x_i in X:
                ret.update(get_first_set(x_i, first_set))
        else: 
            ret.update(first_set[X]["terminals"])

    return ret

#
# Compute the firsts set 
#
def calculate_first_set(productions):
    """
    This is the set of firsts.

    1. If X is a terminal then First(X) is just X!  
    2. If there is a Production X → ε then add ε to first(X) 
    3. If there is a Production X → X1 X2..Xk then add first(X1 X2..Xk) to first(X) 
    4, First(X1 X2..Xk) is either 
        1. First(X1) (if First(X1) doesn't contain ε)
        2. OR (if First(X1) _does_ contain ε) then First (X1 X2..Xk) is everything
           in First(X1) <except for ε > as well as everything in First(X2..Xk)
           3. If First(X1) First(X2)..First(Xk) all contain ε then add ε to
              First(X1 X2..Xk) as well.

    @param productions = {
            "X1" : [has_been_checked, has_epsilon, ["X2X3", "terminals"]],
            "X2" : [has_been_checked, has_epsilon, ["de", "@"]],
            "X3" : [has_been_checked, has_epsilon, ["fg"]],
            .
            .
            "Xk" : [has_been_checked, has_epsilon, ["z"]]
    }
 
    @return first = { 
            "X1" : {
                "terminals" : [], <---- "dft" 
                "compounds" : []  <---- "X2X3"
            }

            "X2" : {
                "terminals" : [], <---- "d@" 
                "compounds" : []  <---- ""
            }
    }
    """
    first = {}

    for key in productions:
        check_production(key, first, productions)

    return first 


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
