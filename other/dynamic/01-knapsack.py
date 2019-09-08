'''
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
'''
def knapsack_problem(weights, values, target_weight):
    if not weights or not values:
        return 0

    if target_weight == 0:
        return 0

    table = [[0]*(target_weight+1) for weight in weights]
    # first fill the first row
    for i in range(0, len(table[0])):
        if weights[0] <= i:
            table[0][i] = 1
    
    for i in range(1, len(table)):
        current_weight = weights[i]
        current_value = values[i]
        for j in range(0, len(table[0])):
            if current_weight > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], current_value + table[i-1][j-current_weight])
    
    # Finding the weights that make up the total weight:
    i, j = len(table)-1, len(table[0])-1
    resultant_weights = []
    while i != 0 and j != 0:
        if i > 0:
            if table[i-1][j] == table[i][j]:
                i = i-1
            else:
                resultant_weights.append(weights[i])
                i = i-1
                j = j-weights[i]
        else:
            resultant_weights.append(weights[0])
            j = 0
    
    print(resultant_weights)
    return table[-1][-1]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
total_weight = 7
print(knapsack_problem(weights, values, total_weight))