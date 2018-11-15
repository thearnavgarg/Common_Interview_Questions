'''

https://www.geeksforgeeks.org/print-increasing-sequences-length-k-first-n-natural-numbers/

'''

'''
k = 3, n = 5

1, 2, 3
1, 3, 4
1, 4, 5
2, 3, 4
..
..
..
3, 4, 5

-------

1, 3

'''

def increasing_k_seq(k, n) -> None:

    def helper(n, i, k, current):
        if len(current) == k:
            print(current)
            return
        for i in range(i, n+1):
            current.append(i)
            helper(n, i+1, k, current)
            current.pop()


    if k == n:
        print([i for i in range(n)])
        return

    current = list()
    helper(n, 1, k, current)

increasing_k_seq(2, 3)