"""
    Problem: Given a list of integers, count and return the number of times each value appears as an array of integers.
"""

def countingSort(arr):
    
    # defining the range of the array
    numbers_to_count = [i for i in range(len(arr))]
    
    # defining the frequency of the elements of the array e.g [1,1,3,2,1] frequency of numbers of 0 to 3 = [0, 0, 0, 0]
    number_frequency = "0" * len(numbers_to_count)
    
    # converting the string element to a list of ints
    counted_arr = [int(i) for i in number_frequency]
    print(len(number_frequency))

    counting = 0
    # counting the numbers
    for i,j in enumerate(numbers_to_count):
        counting += 1
        counted_arr[i] = arr.count(j)
    
    return counted_arr