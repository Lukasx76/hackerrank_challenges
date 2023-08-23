"""
    Problem: Given a list of numbers with an odd number of elements, find the median.
"""

def findMedian(arr):
    # sorting the array 
    arr = sorted(arr)
    
    # defining the median
    median = len(arr) // 2
    
    return arr[median]