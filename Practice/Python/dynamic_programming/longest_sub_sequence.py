def longest_sub_seq(s1='abcdaf', s2='acbcf'):
    s1Len = len(s1)
    s2Len = len(s2)
    table = [[0 for i in range(0, s1Len+1)] for j in range(0, s2Len+1)]
    for i in range(1, s2Len+1):
        for j in range(1, s1Len+1):
            if s2[i-1] == s1[j-1]:
                table[i][j] = max(table[i-1][j], table[i-1][j-1] + 1)
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    print('The table: {}'.format(table))
    print('The lenght of the longest substring: {}'.format(table[s2Len][s1Len]))

if __name__ == '__main__':
    longest_sub_seq()
