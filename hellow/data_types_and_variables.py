#!/usr/bin/python3

#
# Main
#
def main():

    # Various types
    print(type(54))
    print(type("a string"))
    print(type(98.188))
    print(type("3.14"))
    print(type("99"))


    # Python is strong typed
    string_variable = "this is a string"
    integer_variable = 5;

    # The next line would cause a runtime error 
    #print(string_variable + integer_variable)

    # The next line, however prints just fine.
    # Since the variable is now a string
    integer_variable = " don't belive the lies."
    print(string_variable + integer_variable)


    # python has a thing called simultaneos asigement
    var1, var2, var3 = "string", 3.14, 5

    print(var1, var2, var3)


#
# Module check
#
if __name__ == "__main__":
    main()
