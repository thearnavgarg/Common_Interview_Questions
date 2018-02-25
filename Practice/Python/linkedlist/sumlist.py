from linkedlist import LinkedList
from linkedlist import linkedListExamples
from linkedlist import printLinkedList

def addNumbers(num1, num2):
    carryOver = 0
    sumValue = 0
    zeroCheck = 0
    while num1 != None and num2 != None:
        value = num1.getData() + num2.getData() + carryOver
        v = value % 10
        carryOver = int(value / 10)
        sumValue += v*(10**zeroCheck)
        num1 = num1.getNext()
        num2 = num2.getNext()
        zeroCheck +=1
    while num1 != None:
        value = num1.getData() + carryOver
        v = value % 10
        carryOver = int(value / 10)
        sumValue += v*(10**zeroCheck)
        zeroCheck += 1
        num1 = num1.getNext()
    while num2 != None:
        value = num2.getData() + carryOver
        v = value % 10
        carryOver = (value / 10)
        sumValue += v*(10**zeroCheck)
        zeroCheck += 1
        num2 = num2.getNext()
    sumValue += carryOver*(10**zeroCheck)
    return sumValue

if __name__ == '__main__':
    '''
        One easy way to solve this would be just create the
        numbers from the linkedlist and then do integer addition
        BUT, life is not easy... hence, I will take the less
        sought after route. I will add as I am traversing the
        the list. FUCK YEAH. 
    '''
    # number 1
    num1 = LinkedList(7)
    num1.setNext(LinkedList(1))
    num1.getNext().setNext(LinkedList(6))
    num1.getNext().getNext().setNext(LinkedList(1))

    # number 2
    num2 = LinkedList(5)
    num2.setNext(LinkedList(9))
    num2.getNext().setNext(LinkedList(2))

    sumValue = addNumbers(num1, num2)
    print('Sum Value: {}'.format(sumValue))