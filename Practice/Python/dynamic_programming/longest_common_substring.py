'''
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.

Examples :

    Input : X = "abcdxyz", y = "xyzabcd"
    Output : 4
    The longest common substring is "abcd" and is of
    length 4.

    Input : X = "zxabcdezy", y = "yzabcdezx"
    Output : 6
    The longest common substring is "abcdez" and is of
    length 6.

'''

'''
    a   b   c   d   x   y   z
x   0   0   0   0   1   0   0
y   0   0   0   0   0   2   0
z   0   0   0   0   0   0   3
a   1   0   0   0   0   0   0
b   0   2   0   0   0   0   0
c   0   0   3   0   0   0   0
d   0   0   0   4   0   0   0
'''

def longest_common_substring(s1, s2):
    table = [[0 for ele in s1] for ele in s2]

    for i in range(0, len(table[0])):
        s1_ele = s1[i]
        if s2[0] == s1_ele:
            table[0][i] = 1
        else:
            table[0][i] = 0

    for i in range(1, len(table)):
        for j in range(0, len(table[0])):
            s2_ele = s2[i]
            s1_ele = s1[j]
            if s2_ele == s1_ele:
                if j == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = 1+table[i-1][j-1]
            else:
                table[i][j] = 0

    max_len = -((2**32)-1)
    
    for i in range(0, len(table)):
        for j in range(0, len(table[0])):
            if table[i][j] > max_len:
                max_len = table[i][j]

    return max_len

print(longest_common_substring('zxabcdezy', 'yzabcdezx'))
