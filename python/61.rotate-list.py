# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        
        Algorithm:
        1. count number of nodes and find pointer to last node
        2. reduce k by node count
        3. find new start
        4. reorganize list by starting node:
            - point head to new starting node
            - cut list to the left of new starting node
            - connect last node to previous head
        
        """
        # if list is empty or consists of one element
        if not head or not head.next:
            return head
        
        # zero pointer
        zero = head
              
        # count number of nodes
        # and get pointer to last node
        count, last = 1, zero
        while last.next:
            count += 1
            last = last.next
            
        # reduce k by node count 
        k %= count
        
        # if k is a multiple by count
        # return head
        if not k:
            return head
        
        # find a new start node
        new_start = zero
        for _ in range(count - k - 1):
            new_start = new_start.next
            
        # 1. point head to node next to new starting node
        # 2. connect last node to previous head
        # 3. point node previous to new start to None
        # (colloquially cut the list to the left of new starting node) 
        head, last.next, new_start.next = new_start.next, head, None
        
        return head
    