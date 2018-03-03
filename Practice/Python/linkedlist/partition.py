from linkedlist import LinkedList
from linkedlist import printLinkedList

def partitionAlgorithm(head, value=5):
    
    
if __name__ == '__main__':
    head = LinkedList(3)
    head.setNext(LinkedList(5))
    head.getNext().setNext(LinkedList(8))
    head.getNext().getNext().setNext(LinkedList(5))
    head.getNext().getNext().getNext().setNext(LinkedList(10))
    head.getNext().getNext().getNext().getNext().setNext(LinkedList(2))
    head.getNext().getNext().getNext().getNext().getNext().setNext(LinkedList(1))
    printLinkedList(head)
    head = partitionAlgorithm(head)
    printLinkedList(head)