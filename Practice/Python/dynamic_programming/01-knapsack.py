def backtrack(table, w, t):
    numRows = len(w)
    if numRows == 1:
        return [w[0]]
    i = numRows-1
    j = t
    answer = []
    while j != 0:
        current_val = table[i][j]
        if current_val != table[i-1][j]:
            answer.append(w[i])
            j = j - w[i]
        i = i-1
    return answer


def solution(w = [1, 3, 4, 5], v = [1, 4, 5, 7], t = 7):    
    numWeights = len(w)
    table = [[0 for x in range(0, t+1)] for y in range(0, numWeights)]
    # Calculating the first row
    weight = w[0]
    value = v[0]
    for i in range(0, t+1):
        if weight > i:
            table[0][i] = 0
        else:
            table[0][i] = value
    # calculating for the rest of the rows
    for i in range(1, numWeights):
        for j in range(0, t+1):
            weight = w[i]
            value = v[i]
            if weight > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], value + table[i-1][j-weight])
    ansWeights = backtrack(table, w, t)
    return [ansWeights, table[numWeights-1][t]]

if __name__ == '__main__':
    # w = weights, v = values, t = target
    sol = solution()
    print('The weights are: {} \nThe value is: {}'.format(sol[0], sol[1]))
