# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        
        if not l1 or not l2:
            return l1 if not l2 else l2
        
        carryOver = 0
        head = ListNode(0)
        currentHead = head
        
        while l1 or l2:
            l1Value = 0
            l2Value = 0
            if l1:
                l1Value = l1.val
                l1 = l1.next
            if l2:
                l2Value = l2.val
                l2 = l2.next
            
            
            value = (l1Value + l2Value + carryOver) % 10
            carryOver = (l1Value + l2Value + carryOver) // 10
            
            currentHead.next = ListNode(value)
            currentHead = currentHead.next
        
        if carryOver != 0:
            currentHead.next = ListNode(carryOver)
        
        return head.next
