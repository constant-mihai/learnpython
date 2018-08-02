#!/usr/bin/python3

# ripped off of: https://overiq.com/python/3.4/lists-in-python/

#
# Main
#
def main():
    # Numbers is a refernce. Array is alloced on the heap
    numbers = [11, 99, 66, 22]

    type(numbers) # <class 'list'>
    print(numbers) # [11, 99, 66, 22]
    # A list can contain elements of same or different types.
    mixed = ["a string", 3.14, 199]  # list where elements are of different types

    # List Concatenation #
    # List can be joined too using + operator. When operands on 
    # both side are lists + operator creates a new list by combing 
    # elements from both the lists. For example:

    list1 = [1,2,3]  # create list1
    list2 = [11,22,33]  # create list2

    print(id(list1))   # address of list1
    print(id(list2))   # address of list2



    list3 = list1 + list2   # concatenate list1 and list2 and create list3
    print(list3) #    [1, 2, 3, 11, 22, 33]

    # Notice that concatenation doesn't affect the list1 and list2, 
    # their addresses remains the same before and after the concatenation.

    id(list3)  # address of the new list list3
    id(list1)   # address of list1 is still same
    id(list2)   # address of list2 is still same

    # Repetition Operator #
    #We can use * operator with lists too. It's syntax is:

    # sequence * n
    # The * operator replicates the list and then joins them. 
    # Here are some examples:
    list1 = [1, 5]
    list2 = list1 * 4  # replicate list1 4 times and assign the result to list2
    print(list2) #    [1, 5, 1, 5, 1, 5, 1, 5]

    # You can also compare lists
    print(list1 < list2)


    # List comprehension
    cube_list = [ i**3 for i in range(50, 101) ]
    print(cube_list)

    # List comprehension with condition
    even_list = [ i for i in range(1, 10) if i % 2 == 0 ]
    print(even_list)

#
# Module check
#
if __name__ == "__main__":
    main()
