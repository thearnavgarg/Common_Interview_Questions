'''

Checking if a binary tree is symmteric across it's root node

'''

def isSymmetricHelper(root1, root2):
    if not root1 and not root2:
        return True
    
    if not root1 or not root2:
        return False
    
    if root1.data != root2.data:
        return False

    return isSymmetricHelper(root1.left, root2.right) and \
            isSymmetricHelper(root1.right, root2.left)


def isSymmetric(root):
    return isSymmetricHelper(root, root)
