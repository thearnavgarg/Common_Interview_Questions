import linkedlist as ll

def deleteMiddleNode(node):
    if node == None:
        return
    if node.getNext() == None:
        return
    prev = node
    current = node.getNext()
    while current.getNext() != None:
        prev.setData(current.getData())
        prev = prev.getNext()
        current = current.getNext()
    prev.setData(current.getData())
    prev.setNext(None)
    

if __name__ == '__main__':
    head = ll.LinkedList('a')
    head.setNext(ll.LinkedList('b'))
    removeNode = ll.LinkedList('c')
    head.getNext().setNext(removeNode)
    head.getNext().getNext().setNext(ll.LinkedList('d'))
    head.getNext().getNext().getNext().setNext(ll.LinkedList('e'))
    head.getNext().getNext().getNext().getNext().setNext(ll.LinkedList('f'))
    print('Before the algorithm: ', end='')
    ll.printLinkedList(head)
    deleteMiddleNode(removeNode)
    print('After the algorithm: ', end='')
    ll.printLinkedList(head)
    