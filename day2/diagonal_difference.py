"""
    Problem:Given a square matrix, calculate the absolute difference between the sums of its diagonals.

    For example, the square matrix array is shown below:

    1 2 3
    4 5 6
    9 8 9  
"""

def diagonalDifference(arr):

    # i is the line
    # j is the column

    # 00 11 22 02 11 20

    left_to_right_sum = 0
    right_to_left_sum = 0
    
    # left to right the coordinates must be equal
    i = 0
    j = 0

    size_of_inner_arr = len(arr[i])

    # right to left coordinates start at the end of the first inner array
    # j2 is the start of the column of the right to left sum 
    j2 = size_of_inner_arr - 1

    while i < size_of_inner_arr:
        left_to_right_sum += arr[i][j]
        right_to_left_sum += arr[i][j2]
        i += 1
        j += 1
        j2 -= 1

    return abs(left_to_right_sum - right_to_left_sum)


diagonalDifference([[11,2,4],
                    [4,5,6],
                    [10,8,-12]])