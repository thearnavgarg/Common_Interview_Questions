'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

def copyRandomList(head):
    if not head:
        return None
        
    mapper = {None: None}
    newhead = RandomListNode(-1)
    newcurr = newhead
    curr = head
    
    curr = haed

    while curr:
        # we will copy the list. 
        if curr not in mapper:
            mapper[curr] = RandomListNode(curr.label)
        if curr.random not in mapper:
            mapper[curr.random] = RandomListNode(curr.random.label)
        
        newcurr.next = mapper[curr]
        newcurr.next.random = mapper[curr.random]
        curr = curr.next
        newcurr = newcurr.next
    
    
    return newhead.next
