'''

check if the tree is a Binary Search Tree

'''

def isBSTHelper(root, max=1000, min=-1000):
    if not root:
        return True
    if root.data >= max or root.data < min:
        return False
    return isBSTHelper(root.left, root.data, min) and \
            isBSTHelper(root.right, max, root.data)

def isBST(root):
    if not root:
        return True
    return isBSTHelper(root)
