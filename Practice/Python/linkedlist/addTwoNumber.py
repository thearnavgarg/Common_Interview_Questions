'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


Leetcode: Your runtime beats 100.00 % of python3 submissions.

'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carryOver = 0
        head = None
        tail = None
        while l1 != None and l2 != None:
            temp = l1.val + l2.val + carryOver
            value = temp % 10
            carryOver = int(temp / 10)
            newNode = ListNode(value)
            if head == None:
                head = newNode
                tail = head
            else:
                tail.next = newNode
                tail = tail.next
            l1 = l1.next
            l2 = l2.next
        leftOver = None
        if l1 == None:
            leftOver = l2
        else:
            leftOver = l1
        while leftOver != None:
            tempValue = leftOver.val + carryOver
            value = tempValue % 10
            carryOver = int(tempValue / 10)
            newNode = ListNode(value)
            if head == None:
                head = newNode
                tail = head
            else:
                tail.next = newNode
                tail = tail.next
            leftOver = leftOver.next
        if carryOver != 0:
            newNode = ListNode(carryOver)
            tail.next = newNode
        return head