
def solution(coins=[2,3,7,8,10], total=14):
    numCoins = len(coins)
    table = [[False for x in range(0, total+1)] for y in range(0, numCoins)]
    # First Col
    for i in range(0, numCoins):
        table[i][0] = True
    # First Row
    for i in range(1, total+1):
        if coins[0] == i:
            table[0][i] = True
        else:
            table[0][i] = False
    # The rest of the table
    for i in range(1, numCoins):
        for j in range(1, total+1):
            if coins[i] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-coins[i]]
    print('Table: {}'.format(table))
    print('Possibility? {}'.format(table[numCoins-1][total]))

if __name__ == '__main__':
    solution()