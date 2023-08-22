"""
    Problem: Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""

def miniMaxSum(arr):
    
    min_sum = 0
    max_sum = 0

    arr = sorted(arr)

    # finding the min sum excluding the maximum value

    for i in range(0, len(arr) -1 , 1):
        min_sum += arr[i]

    # finding the max sum excluding the minimum value

    for i in range(1, len(arr), 1):
        max_sum += arr[i]

    print(f"{min_sum} {max_sum}")

miniMaxSum([7, 69, 2, 221, 8974])