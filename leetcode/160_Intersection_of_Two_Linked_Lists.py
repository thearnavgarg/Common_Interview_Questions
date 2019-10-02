# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        #################################
        # Helper functions
        
        def move_start_pointer(head, distance):
            current = head
            while distance != 0:
                if not current:
                    return None
                current = current.next
                distance -= 1
            return current
    
    
        def find_intersection(headA, headB):
            while headA and headB:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next
            return None

        #################################
        
        
        # base condition
        if not headA or not headB:
            return None
        
        length_A, length_B = 0, 0
        current_A, current_B = headA, headB
        
        # Calculate the length of the linkedLists. 
        while current_A or current_B:
            if current_A:
                length_A += 1
                current_A = current_A.next
            if current_B:
                length_B += 1
                current_B = current_B.next
        
        print(length_A, length_B)
        current_A, current_B = headA, headB
        
        # find which one is larger in size. 
        if length_A > length_B:
            current_A = move_start_pointer(headA, length_A - length_B)
        elif length_B > length_A:
            current_B = move_start_pointer(headB, length_B - length_A)
        
        if not current_A or not current_B:
            return None
        
        intersection_pointer = find_intersection(current_A, current_B)
        
        if not intersection_pointer:
            return None
        
        return intersection_pointer
        
