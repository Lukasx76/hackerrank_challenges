"""
    Problem: Given a list of integers, count and return the number of times each value appears as an array of integers.
"""

def countingSort(arr):

    frequency_arr = "0" * 100
    frequency_arr = [int(i) for i in frequency_arr]
    arr = sorted(arr)

    for value in arr:
        frequency_arr[value] += 1

    return frequency_arr

print(countingSort([1,1,3,2,1]))