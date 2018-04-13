'''

Given an array [1, 2, 0, 1, 5], and an index point, if the index points to the element
0, then the players wins, else the non-zero positive number at that index specifies how many
spaces left or right he can go.

For example:
INPUT = [1, 2, 0, 1, 5] and 2
OUTPUT: True

INPUT = [1, 2, 0, 1, 5] and 0
OUTPUT = True
move 1 space right from index 0
move 2 space right from index 1
move 1 space left from index 3
arrive at 0 (Winner)

INPUT = [1, 2, 0, 1, 5] and 4
OUTPUT = False
move 5 spaces left --> out of bounds
move 5 spaces right --> out of bounds

'''

def canWinHelper(arr, index, mem):
    if index < 0 or index >= len(arr):
        return False
    if arr[index] == 0:
        return True
    if index in mem:
        return False
    mem.add(index)
    return canWinHelper(arr, index-arr[index], mem) or \
           canWinHelper(arr, index+arr[index], mem)

def canWin(arr, index):
    mem = set()
    return canWinHelper(arr, index, mem)

def main():
    arr = [1, 1, 5, 0, 5]
    arr1 = [1, 2, 0, 1, 5]
    print(canWin(arr, 1))
    print(canWin(arr1, 1))

main()
