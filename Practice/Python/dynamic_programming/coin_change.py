'''

Coining changing problem

total = 13

coins = 7, 2, 3, 6

output = 2 (7, 6)

'''

'''

[0, 1000, 1, 1, 2, 2, 1, 1, 2, 2, 2, 3, 2, 2]
[-1. -1. 1. 2. 1, 2, 3, 0, 3, 1, 2, 1, 3, 3]

[6, 7] and the size = 2

'''

def coin_changing(arr, total):
    table = [1000 for i in range(0, total+1)]
    table[0] = 0
    index_table = [-1 for i in range(0, total+1)]

    for idx, ele in enumerate(arr):
        for i in range(1, len(table)):
            if i >= ele:
                if table[i-ele]+1 < table[i]:
                    index_table[i] = idx
                table[i] = min(table[i], table[i-ele]+1)
    
    solution = []
    
    if index_table[-1] != -1:
        check = total
        while check > 0:
            arr_index = index_table[check]
            solution.append(arr[arr_index])
            check = check - arr[arr_index]
    
    return solution, table[len(table)-1]

print(coin_changing([7, 2, 3, 6], 13))


