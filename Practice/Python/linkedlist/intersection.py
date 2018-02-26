from linkedlist import LinkedList

def linkedListSize(head):
    size = 0
    curr = head
    while curr != None:
        size += 1
        curr = curr.getNext()
    return size

def findIntersection(head1, head2):
    if head1 == None or head2 == None:
        return None
    firstHeadSize = linkedListSize(head1)
    secondHeadSize = linkedListSize(head2)
    largerList, smallerList = None, None
    sizeDiff = abs(firstHeadSize - secondHeadSize)
    if firstHeadSize > secondHeadSize:
        largerList = head1
        smallerList = head2
    else:
        largerList = head2
        smallerList = head1
    while sizeDiff != 0:
        largerList = largerList.getNext()
        sizeDiff -= 1
    while largerList != None and smallerList != None:
        if largerList == smallerList:
            return largerList
        largerList = largerList.getNext()
        smallerList = smallerList.getNext()


if __name__ == '__main__':
    # Testcase 1
    head1 = LinkedList(1)
    head2 = LinkedList(3)
    intersectionNode = LinkedList(4)
    head1.setNext(LinkedList(2))
    head1.getNext().setNext(LinkedList(3))
    head1.getNext().getNext().setNext(intersectionNode)
    head2.setNext(intersectionNode)
    head2.getNext().setNext(LinkedList(5))
    head2.getNext().getNext().setNext(LinkedList(6))

    # Testcase 2
    testHead1 = LinkedList(1)
    testHead2 = LinkedList(10)
    testIntersectionNode = LinkedList(100)
    testHead1.setNext(LinkedList(2))
    testHead1.getNext().setNext(testIntersectionNode)
    testHead2.setNext(LinkedList(20))
    testHead2.getNext().setNext(testIntersectionNode)

    node = findIntersection(testHead1, testHead2)
    print('The interesting node is: {}'.format(node.getData()))