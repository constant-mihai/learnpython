#!/usr/bin/python3

from enum import Enum

#
# Token types
#
class Type(Enum):
    INTEGER = 0,
    PLUS = 1,
    MINUS = 2,
    MUL = 3,
    DIV = 4,
    LPARAN = 5,
    RPARAN = 6,
    BEGIN = 7,
    END = 8,
    SEMI = 9,
    DOT = 10,
    ID = 11,
    ASSIGN = 12,
    EOF = 100 


#
# Token class
#
class Token(object):

    #
    # Ctor
    #
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        self.value = value

    #
    # String representation
    #
    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


#
# Position
#
class Position():
    #
    # Ctor
    #
    def __init__(self, text):
        self.__pos = 0
        self.__text = text
        self.__char = self.__text[self.__pos]
        print("Pos: {}, char: {}".format(self.__pos, self.__char))

    #
    # Peek
    #
    def peek(self):
        if (self.__pos + 1) > (len(self.__text) - 1):
            return None 
        else:
            return self.__text[self.__pos + 1]


    #
    # Advance
    #
    def adv(self, leap):
        self.__pos += leap 
        if self.the_end():
            print("Reachd end Pos: {}, last char: {}"\
                    .format(self.__pos, self.__char))
        else:
            self.__char = self.__text[self.__pos]
            print("Pos: {}, char: {}".format(self.__pos, self.__char))

    #
    # Lesser than
    #
    def __lt__(self, other):
        return self.__pos < other
    def __le__(self, other):
        return self.__pos <= other

    #
    # Greater than
    #
    def __gt__(self, other):
        return self.__pos > other
    def __ge__(self, other):
        return self.__pos >= other

    #
    # Equal
    #
    def __eq__(self, other):
        return self.__pos == other
    def __ne__(self, other):
        return self.__pos != other

    #
    # End of the line 
    #
    def the_end(self):
        return self.__pos >= len(self.__text)

    #
    # Curr
    #
    def char(self):
        return self.__char


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
