#!/usr/bin/python3

#
# Main
#
def main():
    arg1 = "test" 
    print("Before function call, arg1 =", id(arg1))
    func(arg1)
    print("After function call, arg1 =", arg1)


    parrot(1000)                                          # 1 positional argument
    parrot(voltage=1000)                                  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
    print("\n\n\n")

    #parrot()                     # required argument missing
    #parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
    #parrot(110, voltage=220)     # duplicate value for the same argument
    #parrot(actor='John Cleese')  # unknown keyword argument

    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
    print("\n\n\n")

    # Unpacking arguments 
    args = [3, 6]
    range_list = list(range(*args))            # call with arguments unpacked from a list
    print(range_list)                          #[3, 4, 5]
    print("\n\n\n")

    d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    parrot(**d)
    print("\n\n\n")

    for i in updown(3): print(i)

#
# Functions
#
def func(para1):
    """
        Params are passed by reference.
        When an immutable param is modified
        new memory is allocates and the parameter
        points to the new memory
    """
    print("Inside function call, para1 =", id(para1))
    para1 += " test"# increment para1 by 100
    print("Inside function call, after addition=", id(para1))


#
# Positional and keword
#
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

#
# Positional and keword
#
def cheeseshop(kind, *arguments, **keywords):
    """
    * - list of positional arguments
    ** - dictionary of keyword arguments
    """
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

#
# Lambda functions
#
def make_incrementor(n):
    """
    lambda parameters: expression
    """
    return lambda x: x + n


#
# Generators
#
def updown(N):
    for x in range(1, N):
        yield x
    for x in range(N, 0, -1):
        yield x

#
# Module check
#
if __name__ == "__main__":
    main()
