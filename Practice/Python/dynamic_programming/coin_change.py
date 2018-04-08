
def solution(coins=[7,2,3,6], total=13):
    numTable = [1000 for x in range(0, total+1)]
    numTable[0] = 0
    coinTable = [-1 for x in range(0, total+1)]
    for i in range(0, len(coins)):
        for j in range(1, total+1):
            if coins[i] <= j:
                value = min(numTable[j], 1+numTable[j-coins[i]])
                if numTable[j] != value:
                    numTable[j] = value
                    coinTable[j] = i
    print('Table: {}'.format(numTable))
    print('The min number of coins: {}'.format(numTable[total])) 
    tmp = total
    coinList = []
    while tmp != 0:
        coinList.append(coins[coinTable[tmp]])
        tmp = tmp - coins[coinTable[tmp]]
    print('The coins are: {}'.format(coinList))

if __name__ == '__main__':
    solution()