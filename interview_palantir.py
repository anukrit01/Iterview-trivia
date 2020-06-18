# Palantir
'''
You have an array of strings - crypt, the cryptarithm, and an array containing the mapping
of letters and digits - solution. The array crypt will contain three non-empty strings that
follow the structure: [word1, word2, word3], which should be interpreted as the 
word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of them of the letters in the cryptarithm with
digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers
with leading zeroes, the answer is true. If it does not become a valid arithmetic solution,
the answer is false.

NOTE that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Sample Input:
                crypt = ['SEND', 'MORE', 'MONEY']
                solution = [['O', '0'],
                            ['M', '1'],
                            ['Y', '2'],
                            ['E', '5'],
                            ['N', '6'],
                            ['D', '7'],
                            ['R', '8'],
                            ['S', '9']]
When you decrypt 'SEND', 'MORE', and 'MONEY' using the mapping given in crypt:
you get 9567 + 1085 = 10652
which is correct and a valid arithmetic equation.

Sample Output:
              isCryptSolution(crypt, solution) = true
'''

def isCryptSolution(crypt, solution):
    solution = dict(solution)   # Convert into dictionary so that the mapping is easy.
    li = []
    for i in crypt:
        new = ""    # Empty string
        # Mapping letter to a number and creating a string for ex. 'SEND' = '9567'
        for j in range(len(i)):
            new += solution[i[j]]
        li.append(new)  # inserting all new strings in a list

    for i in range(len(li)):    # checking if first character is '0'
        if li[i][0] == '0' and len(li[i]) > 1:
            return False
        else:
            pass
    
    # Checking for word1 + word2 = word3
    if (int(li[0]) + int(li[1])) == int(li[2]):
        return True
    else:
        return False

# Test
crypt = ['SEND', 'MORE', 'MONEY']
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
print(isCryptSolution(crypt, solution))