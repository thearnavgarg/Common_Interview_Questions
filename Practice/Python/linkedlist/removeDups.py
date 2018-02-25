from linkedlist import LinkedList
from linkedlist import printLinkedList

def removeDuplicates(head):
    dupCatcher = set()
    prev = None
    current = head
    while current != None:
        if not current.getData() in dupCatcher:
            dupCatcher.add(current.getData())
            prev = current
            current = current.getNext()
        else:
            prev.setNext(current.getNext())
            current = current.getNext()

if __name__ == '__main__':
    head = LinkedList(1)
    head.setNext(LinkedList(2))
    head.getNext().setNext(LinkedList(2))
    head.getNext().getNext().setNext(LinkedList(3))
    head.getNext().getNext().getNext().setNext(LinkedList(3))
    print('Before algorithm: ', end='')
    printLinkedList(head)
    removeDuplicates(head)
    print('After algorithm: ', end='')
    printLinkedList(head)
    