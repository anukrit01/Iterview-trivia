#Amazon.com

'''
Given a string S consisting of small English letters, find and return the first
instance of a non repeating character in it. If there is no such 
repeating character, return '-'.
Sample Input: aaabcccdeeef
Sample Output: b
'''

S = input('Enter a String: ')
count_dict = {}     #Dictionary to keep count of chars

for i in S:     #inserting char:count
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1
#print(count_dict)
    
flag = False
for i in S:     #print the first non repeating char
    if count_dict[i] > 1:
        pass
    elif count_dict[i] == 1:
        print(i)
        flag = True
        break

if not flag:        #print '-' if no non-repeating char
    print('-')