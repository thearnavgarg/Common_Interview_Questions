'''
Find the longest common subsequence

string1 = 'abcdaf'
string2 = 'acbcf'

output = 'abcf' ==> len 4

'''

'''
scratch work

    a   b   c   d   a   f
a   1   1   1   1   1   1
c   1   1   2   2   2   2
b   1   2   2   2   2   2
c   1   2   3   3   3   3
f   1   2   3   3   3   4

'''

def longest_common_subsequence(string1, string2):
    table = [[0 for i in range(0, len(string1)+1)] for j in range(0, len(string2)+1)]
    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            s2_ele = string2[i-1]
            s1_ele = string1[j-1]
            if s2_ele == s1_ele:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[len(table)-1][len(table[0])-1]

print(longest_common_subsequence('abcdaf', 'acbcf'))
