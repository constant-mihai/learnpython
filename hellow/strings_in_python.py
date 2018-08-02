#!/usr/bin/python3

# ripped off of: https://overiq.com/python/3.4/

#
# Main
#
def main():
    achar = 'a'          # string containing a single character
    type(achar)          #<class 'str'>
    type("a string")     # string containing multiple characters
                         # <class 'str'>
    len("a string")      #    8

    s = "a long string"
    len(s)               #    13
    len("")              #     0

    # Python has a string repetition operator
    s = "www " * 5  # repeat "www " 5 times
    print(s) #    'www www www www www '
    print("We have got some", "spam" * 5) #    We have got some spamspamspamspamspam


    # Just like perl you can get strings using the retrieve operator []
    # Just like perl you can get letters from the end of the string using
    # the -n
    
    test_string = "This a test string"

    print(test_string[-1]) # g

    # You can also slice strings
    s = "markdown"
    print(s[0:3])  # get a slice of string starting from index 0 to 3, not including the character at index 3
                   #     'mar'
    print(s[2:5])  # get a slice of string starting from index 2 to 5, not including the character at index 5
                   #     'rkd'


    # ord() and chr()
    print(ord("a"))  # print the ASCII value of character a
              # 97
    print(ord("5"))  # print the ASCII value of character 5
              # 53
    print(chr(97))   # print the character represented by ASCII value 97
              # 'a'
    print(chr(53))   # print the character represented by ASCII value 53
              # '5'


    #print("first string", end="$")
    #print("second string", end="$")

    #print("first", "second", "third", sep="#")


    # Strings are Immutable #
    # String objects are immutable. It means that we can't 
    # change the content of a string object after it is created. Consider the following example:
    s = "hello"
    print(id(s))

    # Following line will crash the script
    # s[0] = y

    # Formating
    print(format("Python", ">10s"))

    mylist = [1,2,3]
    print("A list: %s" % mylist)

    data = ("John", "Doe", 53.44)
    format_string = "Hello  %s %s %d"

    print(format_string % data)



#
# Module check
#
if __name__ == "__main__":
    main()
