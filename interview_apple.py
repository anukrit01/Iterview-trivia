#Amazon, Microsoft, Apple
'''
You are given an n x n 2D matrix that represents an image.
Rotate the image by 90 degrees(clockwise).

Sample Input: [[1,2,3]
               [4,5,6]
               [7,8,9]]

Sample Output: [[7,4,1]
                [8,5,2]
                [9,6,3]]
'''

li = [[1,2,3],
      [4,5,6],
      [7,8,9]]

#First transpose the matrix
trans_li = [list(row) for row in zip(*li)]
#print(trans_li)

'''
Now we just have to replace last column with first
while iterating towards inside. For example, if it was
4x4 matrix, it would replace col 3 with col 0 and col 2
with col 1.
'''

#swapping
for i in range(len(li)):
    for j in range(len(li)//2):
        trans_li[i][j], trans_li[i][len(li)-1-j] = trans_li[i][len(li)-1-j], trans_li[i][j]

print(trans_li) 