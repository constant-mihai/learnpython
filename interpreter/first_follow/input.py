#!/usr/bin/python3

#
# Main
#
def main():
    pass

def input_prod():
    productions = {}
    print("Give the production rules:")
    while True: 
        prod = input("Production:")
        if prod == "EOF" or prod == "eof":
            break

        if prod in productions:
            print("The production rule \"" + prod + "\" has already been defined")
            continue
        
        if (len(prod) > 1 and prod != "EOF") or \
           prod.isalpha() is not True or \
           prod.isupper() is not True: 
               raise Exception("Wrong input arguments")

        print("Introduce the production strings.\n" + \
              "Separate with space.\n" + \
              "If the production contains the empty string\n" + \
              "end the list with the empty char: @ ")
        prod_string = input("Production strings:")

        prod_string_array = prod_string.split(' ')
        productions[prod] = [False, False, prod_string_array]
        print(productions)

    return productions

#
# Module check
#
if __name__ == "__main__":
    main()
