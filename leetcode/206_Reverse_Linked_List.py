# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        newHead = stack.pop()
        currentNode = newHead
        while stack:
            node = stack.pop()
            currentNode.next = node
            currentNode = currentNode.next
        
        currentNode.next = None
        return newHead

