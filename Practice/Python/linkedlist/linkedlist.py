import random

class LinkedList:
    def __init__(self, data=0):
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data
    
    def setNext(self, node):
        self.next = node
        

def printLinkedList(node):
    while node != None:
        print('{} -> '.format(node.getData()), end='')
        node = node.getNext()
    print ('NULL')


def createLinkedList(size):
    random.seed()
    data = random.randrange(1, 9)
    head = LinkedList(data)
    tmp = head
    for i in range(0, size):
        data = random.randrange(1, 9)
        newNode = LinkedList(data)
        tmp.setNext(newNode)
        tmp = tmp.getNext()
    return head

def linkedListExamples():
    storeList = []
    #edge cases
    head = LinkedList(1)
    storeList.append(head)
    storeList.append(None)
    storeList.append(createLinkedList(5))
    storeList.append(createLinkedList(4))
    storeList.append(createLinkedList(10))
    return storeList