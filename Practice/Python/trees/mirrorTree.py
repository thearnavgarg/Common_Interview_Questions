'''

Mirror the tree. 

'''

def mirrorTree(root):
    if not root:
        return None
    if not root.left or not root.right:
        return root

    left = mirrorTree(root.left)
    right = mirrorTree(root.right)

    root.left = right
    root.right = left

    return root




