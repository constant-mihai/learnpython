#!/usr/bin/python3

import input as inpt
import first as firfol 

#
# Main
#
def main():
    productions = inpt.input_prod()
    first = firfol.first(productions)

    print(first)


#
# Module check
#
if __name__ == "__main__":
    main()
