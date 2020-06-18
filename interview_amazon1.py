# Amazon
'''
You are given a string, write a function to encode it.

Sample Input 1: aabbcdddeaaccde
Sample Output 1: a2b2c1d3e1a2c2d1e1

Sample Input 2: ab
Sample Output 2: a1b1
'''

def encode(s):
    st = ''      # create an empty string
    n = len(s)   # length of actual string
    count = 1    # count the number of times we've seen a particular character
    i = 1        # comparator for previous character

    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s + '1'

    while i < n:            # iterate over the whole string
        if s[i] == s[i-1]:  # encountering similar characters and hence count will be increased
            count += 1
        else:
            st += s[i-1] + str(count)   #concatenating the character with its count
            count = 1
        i += 1 

    st += s[i-1] + str(count)   # concatenating remaining character and the count
    return st                   # return the new string

# Test
print(encode('bbbcnggaafgn'))