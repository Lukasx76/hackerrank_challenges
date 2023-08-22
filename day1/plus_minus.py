"""
    Problem: Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
"""

def plusMinus(arr):
    # finding the number of positives
    positives = [number for number in arr if(number > 0)]

    # finding the number of negatives
    negatives = [number for number in arr if(number < 0)]

    # finding the zeros 
    zeros = [number for number in arr if(number == 0)]

    # printing the result
    output = f"""{(len(positives)/len(arr)):.6f}\n{(len(negatives)/len(arr)):.6f}\n{(len(zeros)/len(arr)):.6f}"""

    print(output)