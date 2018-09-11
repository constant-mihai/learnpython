#!/usr/bin/python3

from enum import Enum

#
# Message types
#
class Type(Enum):
    HELLO = 0,
    BYE = 1,
    TXT = 2

#
# Message class
#
class Message(object):
    #
    # Ctor
    #
    def __init__(self, m_from, m_to, m_type, m_length, m_value):
        self.m_from = m_from
        self.to = m_to
        self.type = m_type
        self.length = m_length
        self.value = m_value

    #
    # Pretty print
    #
    def __str__(self):
        ret = "From: " + str(self.m_from) + "\n"
        ret = ret + "To: " + str(self.to) + "\n" 
        ret = ret + "\tType: " + str(self.type) + "\n"
        ret = ret + "\tLength: " + str(self.length) + "\n"
        ret = ret + "\tValue: " + str(self.value) + "\n"
        return ret

    #
    # Add text
    #
    def text(self, text):
        pass

    #
    # Deserialize
    #
    def deserialize(self, data):
        self.m_from = m_from
        self.to = m_to
        self.type = m_type
        self.length = m_length
        self.value = m_value
    

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
