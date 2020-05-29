#GOOGLE
'''
Given two arrays a, b consisting of integers and an integer target value 'v'.
Determine whether there is a pair of numbers, where one number is taken from
a and other from b, that can be added together to get a sum of v.
Return True if such a pair exists, otherwise return False.

Sample Input: a = [1,2,3] b = [1,40,5]
              v = 42
Sample Output: True
Explanation: [2,40] -> 2 + 40 -> 42.
'''

a = list(map(int, input('Enter the First Array: ').split()))
b = list(map(int, input('Enter the Second Array: ').split()))
v = int(input('Enter the Target Value: '))
complements = set()

flag = True

for i in a:
    value = v - i       #42 - i
    complements.add(value)
#print(complements)

for i in b:         #Check whether any element of b is present in set-complements
    if i in complements:
        print(True)
        flag = True
        break
    else:
        flag = False
if not flag:
    print(False)