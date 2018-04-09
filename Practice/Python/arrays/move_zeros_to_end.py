"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]
The time complexity of the below algorithm is O(n).
"""

'''

scratch work

INPUT: [false, 1, 0, 1, 2, 0, 1, 3, "a"]
OUTPUT: [false, 1, 1, 2, 1, 3, "a", 0, 0]

'''


'''

You can create a new array and transfer elements one by one
That would be a time to space tradeoff.
'''
def move_zeros(arr):
    counter = 0
    for idx, ele in enumerate(arr):
        if ele is 0:
            arr.pop(idx)
            counter += 1
    for i in range(counter):
        arr.append(0)
    return arr

def main():
    arr = [False, 1, 0, 1, 2, 0, 1, 3, "a"]
    print(move_zeros(arr))
    
main()