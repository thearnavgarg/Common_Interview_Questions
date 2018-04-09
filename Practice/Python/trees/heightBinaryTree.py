'''

Height of Binary Tree

'''
def height_tree(root):
    if not root:
        return 0
    left = height_tree(root.left)
    right = height_tree(root.right)
    return max(left, right) + 1