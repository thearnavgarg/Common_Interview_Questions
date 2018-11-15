'''

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be
changed.
'''
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        
        first, second = head, head.next
        second.next, first.next = first, second.next
        head = second
        while True:
            prev = first
            first = first.next
            if not first:
                break
            second = first.next
            if not second:
                break
            second.next, first.next = first, second.next
            prev.next = second
        return head
            