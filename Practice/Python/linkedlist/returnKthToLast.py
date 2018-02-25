import linkedlist as ll

def findLinkedListSize(head):
    size = 0
    current = head
    while current != None:
        size += 1
        current = current.getNext()
    return size

# 1 -> 2 -> 3 -> 4 -> 5
# size = 5 and k = 3 (we can the 3rd element)
# 
def returnkthtolast(head, k):
    size = findLinkedListSize(head)
    if size < k:
        return None
    traverseLen = size-k+1
    element = 0
    current = head
    for i in range(0, traverseLen):
        element = current.getData()
        current = current.getNext()
    return element


if __name__ == '__main__':
    examples = ll.linkedListExamples()
    k = 3
    for head in examples:
        print('Before algorithm: ', end='')
        ll.printLinkedList(head)
        element = returnkthtolast(head, k)
        print('After algorithm: {}'.format(element))
