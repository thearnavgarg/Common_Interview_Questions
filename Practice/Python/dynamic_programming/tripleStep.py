'''
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
'''

def tripleStep(n, mem):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if mem[n] != -1:
        return mem[n]
    mem[n] = tripleStep(n-1, mem) + tripleStep(n-2, mem) + tripleStep(n-3, mem)
    return mem[n]

def main():
    n = 3
    mem = [-1 for i in range(n+1)]
    print(tripleStep(n, mem))

if __name__ == '__main__':
    main()