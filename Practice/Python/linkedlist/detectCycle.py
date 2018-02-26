from linkedlist import LinkedList

def getLoopStart(head):
    if head == None or head.getNext() != None:
        return None
    turtle = head
    hare = head
    isLoop = False
    while turtle.getNext() != None or hare.getNext().getNext() != None:
        turtle = turtle.getNext()
        hare = hare.getNext().getNext()
        if turtle == hare:
            isLoop = True
            break
    if not isLoop:
        return None
    turtle = head
    while turtle != hare:
        turtle = turtle.getNext()
        hare = hare.getNext()
    return turtle
    

if __name__ == '__main__':
    # Testcase 1
    head = LinkedList(1)
    head.setNext(LinkedList(2))
    loopStart = LinkedList(3)
    head.getNext().setNext(loopStart)
    head.getNext().getNext().setNext(LinkedList(4))
    head.getNext().getNext().getNext().setNext(LinkedList(5))
    head.getNext().getNext().getNext().getNext().setNext(loopStart)
    node = getLoopStart(head)  
    
    # Testcase 2
    head = LinkedList(1)
    head.setNext(LinkedList(2))
    node = getLoopStart(head)
    
    if node != None:
        print('The intersection node is: {}'.format(node.getData()))
    else:
        print('There is no loop')
