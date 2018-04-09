'''
searching a value in a binary search tree

'''

def solution(root, value):
    if not root:
        return None
    if root.data == value:
        return root
    if value > root.data:
        return solution(root.right)
    else:
        return solution(root.left)