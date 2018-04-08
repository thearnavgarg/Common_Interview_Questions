'''
Code Implementation of Inorder, Postorder and Preorder

'''
from queue import Queue

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.left)
    inorder(root.right)


def preorder(root):
    if not root:
        return None
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return None
    postorder(root.left)
    postorder(root.right)
    print(root.data)


def level_order(root):
    if not root:
        return None
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.data)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
