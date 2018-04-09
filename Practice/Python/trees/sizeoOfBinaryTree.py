'''

Finding the size of the binary tree

'''

def solution(root):
    if not root:
        return 0
    return solution(root.left) + solution(root.right) + 1
    