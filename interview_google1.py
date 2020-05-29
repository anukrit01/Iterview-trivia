#Google
'''
Given an array a that contains only numbers in the range from 1 to a.length,
find the first duplicate number for which the second occurrence has the
minimal index. In other words, if there are more than one dupplicated numbers,
return the number for which the second occurrence has a smaller index than
the second occurrence of the other number does. If there are no such 
elements, return -1.

Sample Input: a = [2, 1, 3, 5, 3, 2]

Sample Output: FirstDuplicate(a) = 3

There are two duplicates: number 2 and 3. The second occurrence of 3 has
a smaller index than the second occurrence of 2 does, so the answer is 3.
'''

def FirstDuplicate(a):
    dic = {}

 for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        return i
 else:
    return -1