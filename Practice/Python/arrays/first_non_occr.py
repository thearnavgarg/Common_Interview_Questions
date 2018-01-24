def main():
    s = 'aaaaaaac'
    A = [-1]*26
    for index, char in enumerate(s):
        pos = ord(char) - ord('a')
        if A[pos] != -1:
            A[pos] = -2
        if A[pos] == -1:
            A[pos] = index
    min = -2
    for ele in A:
        if ele < 0:
            continue
        elif min < 0:
            min = ele
        elif ele < min:
            min = ele
    if min < 0:
        print('-')
    else:
        print(s[min])

if __name__ == '__main__':
    main()
