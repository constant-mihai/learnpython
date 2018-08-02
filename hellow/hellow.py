#!/usr/bin/python3

#
# Main
#
def main():
    print("Starting main.")
    print("Choose lesson:")
    print(" 0. Introduction")
    print(" 1. Types and Variables")
    print(" 2. Numbers in python")
    print(" 3. Strings in python")
    print(" 4. Lists")
    print(" 5. Functions")
    print(" 6. Modules")
    print(" 7. Objects and classes")


    option = input("Option: ")

    if option == '0':
        chapter_introduction()
    elif option == "1":
        chapter_variables()
    elif option == "2":
        chapter_numbers_in_python()
    elif option == "3":
        chapter_strings_in_python()
    elif option == "4":
        chapter_lists_in_python()
    elif option == "5":
        chapter_functions_in_python()
    elif option == "6":
        chapter_modules_in_python()
    elif option == "7":
        chapter_classes_in_python()

#
# chapter : Introduction
#
def chapter_introduction():
    print("0. Introduction")

    print(" a) What is Python?")
    print(" b) Python implementations.")
    subch = input("Choose subject:")

    if subch == 'a':
        print(" a) What is Python")
        print(("Python is high-level interpreted *TODO(check the compiled AND"
                "intepreted thing) language"))
        print("Its also strongly typed.")
    elif subch == 'b':
        print(" b) Python implementations")
        print("Cpython, jython, PyPy, aso")
    else:
        print(" Option unavailable")


#
# chapter : Variables
#
def chapter_variables():
    print("1. Data types and Variables")
    f = open("data_types_and_variables.py", "r");
    contents = f.read()
    print(contents)

#
# chapter : Numbers
#
def chapter_numbers_in_python():
    print("2. Numbers in python")
    f = open("numbers_in_python.py", "r")
    contents = f.read()
    print(contents)

#
# chapter : Strings 
#
def chapter_strings_in_python():
    print("3. Strings in python")
    print(" a) Strings:")
    print(" b) String Methods:")

    subch = input("Choose subject:")

    if subch == 'a':
        f = open("strings_in_python.py")
        print(f.read())
    elif subch == 'b':
        f = open("string_methods_in_python.py")
        print(f.read())
    else:
        print(" Option unavailable")

#
# chapter : Lists 
#
def chapter_lists_in_python():
    print("4. Lists")
    print(" a) Lists")
    print(" b) List Methods:")
    subch = input("Choose subject:")

    if subch == 'a':
        f = open("lists_in_python.py")
        print(f.read())
    elif subch == 'b':
        f = open("list_methods_in_python.py")
        print(f.read())
    else:
        print(" Option unavailable")

#
# chapter : Functions 
#
def chapter_functions_in_python():
    print("5. Functions")
    f = open("functions_in_python.py")
    print(f.read())

#
# chapter : Modules 
#
def chapter_modules_in_python():
    print("6. Modules")
    f = open("modules_in_python.py")
    print(f.read())

#
# chapter : Classes 
#
def chapter_classes_in_python():
    print("7. Classes")
    f = open("objects_and_classes_in_python.py")
    print(f.read())

#
# Module check
#
if __name__ == "__main__":
    main()
