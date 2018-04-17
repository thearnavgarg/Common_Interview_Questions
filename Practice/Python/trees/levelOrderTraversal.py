'''

Level order traversal for linked list. 

'''

import Queue

def levelOrderTraversal(root):
    if not root:
        print('No Tree')
        return
    
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)



