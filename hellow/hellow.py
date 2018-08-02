#!/usr/bin/python3

DESCR, CODE = 0, 1

hellow = {
        "Introduction" : 
        {
            "What is Python?" : 
            [ 
                ("Python is high-level interpreted *TODO(check the compiled AND"
                "intepreted thing) language"),
                None
            ],
            "Python implementations" : 
            [
                "Cpython, jython, PyPy, aso", None
            ],

        },
        "Logging":
        {
            "Intro in logging":
            [
                ("Logging is cool. need to actually use txt files here\n"
                "The logging first file is from:" 
                "https://github.com/CoreyMSchafer"),
                "logging_test.py"
            ],
            "More complicated logging":
            [
                ("Second logging file is still from:"
                "https://github.com/CoreyMSchafer",),
                "more_logging_test.py"

            ]
        },
        "Data types and Variables":
        {
            "Some text about data types here":
            [
                "descr",
                "data_types_and_variables.py"
            ]
        },
        "Numbers in python":
        {
            "Numbers in python":
            [
                "descr",
                "numbers_in_python.py"
            ]
        },
        "Strings in python":
        {
            "Strings in python":
            [
                "descr",
                "strings_in_python.py"
            ],

            "String methods in python":
            [
                "descr",
                "string_methods_in_python.py"
            ]
        },
        "Lists":
        {
            "Lists in python":
            [
                "descr",
                "lists_in_python.py"
            ],

            "List methods in python":
            [
                "descr",
                "list_methods_in_python.py"
            ]
        },
        "Dictionaries":
        {
            "Dictionaries in python":
            [
                "descr",
                "dictionaries_in_python.py"
            ],

            "Dictionarie methods in python":
            [
                "descr",
                "dictionary_methods_in_python.py"
            ]
        },
        "Functions":
        {
            "Functions in python":
            [
                "descr",
                "functions_in_python.py"
            ]
        },
        "Modules":
        {
            "Modules in python":
            [
                "descr",
                "modules_in_python.py"
            ]
        },
        "Classes":
        {
            "Clases in python":
            [
                "descr",
                "objects_and_classes_in_python.py"
            ]
        },

        
}

alphabet = "abcdefghijklmnopqrstuvwxyz" 

#
#
#
def get_i_from_alphabet(alpha):
    if len(alpha) != 1:
        raise Exception("len is not 1")

    if alpha.isalpha() is False:
        raise Exception("is not alpha")

    alpha = alpha.lower()

    i = 0
    while alphabet[i] != "z": 
        if alphabet[i] == alpha: return i
        i+=1

    raise Exception("This should not happen")

#
# Print description
#
def print_description(key, subkey):
    if key == None or subkey == None:
        raise Exception("Should not be null")

    descr = hellow[key][subkey][DESCR]
    if descr is None:
        print("Description is missing!") 
    else:
        print(descr);

#
# Print file
#
def print_file(key, subkey):
    if key == None or subkey == None:
        raise Exception("Should not be null")

    code = hellow[key][subkey][CODE]
    if code is None:
        print("Code file is missing!")
    else:
        f = open(code, "r");
        print(f.read())

#
# Automatic
#
def automatic():
    while True:
        i = 0
        associate = []
        associate_subchapter = []
        for key in hellow:
            associate.append(key)
            print("{}. {}".format(i, key))
            i+=1

        option = input("Chapter: ")

        i = 0
        opt_int = int(option)
        print("{}. {}".format(opt_int, associate[opt_int]))
        key = associate[opt_int]
        for subch in hellow[key]:
            associate_subchapter.append(subch)
            print("\t{}) {}".format(alphabet[i], subch))
            i+=1

        subch_alpha = input("SubChapter: ")
        subch_int   = get_i_from_alphabet(subch_alpha)

        subkey = associate_subchapter[subch_int]
        print("\t{}) {}".format(alphabet[subch_int], subkey))
        print_description(key, subkey);
        print_file(key, subkey)

#
# Main
#
def main():
    automatic()
    
#
# Module check
#
if __name__ == "__main__":
    main()
