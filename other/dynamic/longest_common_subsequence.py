'''
https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/
'''

def longest_common_subsequence(string1, string2):
    if not string1 or not string2:
        return None
    
    table = [[0]*(len(string1)+1) for char in string2]

    for i in range(1, len(table[0])):
        if string2[0] == string1[i-1]:
            table[0][i] = 1
        else:
            table[0][i] = table[0][i-1]
    
    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            if string1[j-1] == string2[i]:
                table[i][j] = 1+table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    
    return table[-1][-1]

print(longest_common_subsequence('abcdaf', 'acbcf'))
    
