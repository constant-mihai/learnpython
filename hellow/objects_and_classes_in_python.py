#!/usr/bin/python3

#
# Main
#

class Dog:

    # tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []      # correct use of a class variable

    def add_trick(self, trick):
        self.tricks.append(trick)


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


#
# Derived class
#
class Fancy_bag(Bag):
    """
    Excerpt from: https://docs.python.org/3.6/tutorial/classes.html
    Execution of a derived class definition proceeds the same as for a base class. 
    When the class object is constructed, the base class is remembered. 
    This is used for resolving attribute references: if a requested attribute is not 
    found in the class, the search proceeds to look in the base class. 
    This rule is applied recursively if the base class itself is derived from some other class.
    """
    def __init__(self):
        pass

#
# Multiple inheritence 
#
class Abomination(Bag, Dog):
    """
    For most purposes, in the simplest cases, you can think of the search for
    attributes inherited from a parent class as depth-first, left-to-right, not
    searching twice in the same class where there is an overlap in the
    hierarchy. Thus, if an attribute is not found in DerivedClassName, it is
    searched for in Base1, then (recursively) in the base classes of Base1, and
    if it was not found there, it was searched for in Base2, and so on.

    In fact, it is slightly more complex than that; the method resolution order
    changes dynamically to support cooperative calls to super(). This approach is
    known in some other multiple-inheritance languages as call-next-method and is
    more powerful than the super call found in single-inheritance languages.

    Dynamic ordering is necessary because all cases of multiple inheritance exhibit
    one or more diamond relationships (where at least one of the parent classes can
            be accessed through multiple paths from the bottommost class). For
    example, all classes inherit from object, so any case of multiple inheritance
    provides more than one path to reach object. To keep the base classes from being
    accessed more than once, the dynamic algorithm linearizes the search order in a
    way that preserves the left-to-right ordering specified in each class, that
    calls each parent only once, and that is monotonic (meaning that a class can be
            subclassed without affecting the precedence order of its parents). Taken
    together, these properties make it possible to design reliable and extensible
    classes with multiple inheritance. For more detail, see
    https://www.python.org/download/releases/2.3/mro/.
    """
    def __init__(self):
        pass



def main():
    pass

#
# Module check
#
if __name__ == "__main__":
    main()
