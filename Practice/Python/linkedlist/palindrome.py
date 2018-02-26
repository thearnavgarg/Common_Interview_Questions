from linkedlist import printLinkedList
from linkedlist import LinkedList

def isPalindromeHelper(head, tail):
    if not head:
        return None
    if head.getNext() == None:
        return None
    if tail == None:
        return [head, True]
    [head, result] = isPalindromeHelper(head, tail.getNext())
    if tail.getData() == head.getData():
        result = result and True
    else:
        result = result and False
    head = head.getNext()
    return [head, result]

def isPalindrome(head):
    tail = head
    start = head
    theTailStopper = set()
    return isPalindromeHelper(start, tail)

if __name__ == '__main__':
    head = LinkedList('a')
    head.setNext(LinkedList('b'))
    head.getNext().setNext(LinkedList('c'))
    head.getNext().getNext().setNext(LinkedList('b'))
    head.getNext().getNext().getNext().setNext(LinkedList('a'))
    result = isPalindrome(head)
    print('The answer is: {}'.format(result[1]))