# Google
'''
Given an array A of integers, return True if and only
if it is a valid mountain array.
Mountain Array : is an array, which after plotting on graph shows
a mountain like structure. Starting from a less value and increasing till
a point and then again decreasing. But it did not contain same value anywhere.

Sample Input1 : [0, 2, 3, 4, 5, 2, 1]
Sample Output1 : True

Sample Input2 : [0, 2, 3, 4, 5]
Sample Output2 : False
'''

def mountArr(arr):
    n = len(arr) - 1
    i = 0

    # loop through the array and increament i if given condition satisfies
    # Our goal is to find the point after which numbers start decreasing
    while i < n and arr[i] < arr[i+1]:
        i += 1

    # if i == 0, means previously conditions weren't satisfied
    # if i == n, means the array is in increasing order only
    # Hence return False.

    if i == 0 or i == n:
        return False

    # if we get through the previous conditions
    # we'll look for a decreasing order
    # if the conditions are satisfied
    # then we'll be having i at the last index
    # we'll return True
    # if not then return False

    while i < n and arr[i] > arr[i+1]:
        i += 1
    
    return i == n

# Test
arr = [0, 2, 3, 5, 4, 0]
print(mountArr(arr))