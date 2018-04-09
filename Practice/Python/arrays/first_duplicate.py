'''
Find the first duplicate element in the array
in: [2, 3, 3, 1, 5, 2]
output: 3
'''
if __name__ == '__main__':
    arr = [2, 3, 3, 1, 5, 2]
    dupSet = set()
    for ele in arr:
        if ele in dupSet:
            print(ele)
            break
        else:
            dupSet.add(ele)