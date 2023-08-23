"""
    Problem: Given an array of integers, where all elements but one occur twice, find the unique element.
"""

def lonelyinteger(a):
    # defining a data structure to store the number of elements present in the array
    number_of_elements = {}

    # removing duplicates through a set
    unique_values_to_iterate = set(a)

    for i in unique_values_to_iterate:
        number_of_elements[i] = a.count(i)

        # searching for the unique element
        if number_of_elements.get(i) == 1:
            return i
        else:
            continue
    return "There is no unique element"

print(lonelyinteger([1,2,3,4,3,2,1]))