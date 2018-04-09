'''

Checking to see if two binary tree are exactly the same or not.

'''

def solution(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.data == root2.data and
            solution(root1.left, root2.left) and
            solution(root1.right, root2.right)