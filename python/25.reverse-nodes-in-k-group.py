# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(node: Optional[ListNode]) -> Optional[ListNode]:
            tail = node
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev, tail
        
        if k == 1:
            return head
                
        i = 1
        res = ListNode()
        res.next = head
        
        prev = res
        node = head
        
        while node:
            if i % k == 0:
                # temporarily cut part of list for reversion
                tmp = node.next
                node.next = None
                # reverse part of list
                prev.next, node = rev(prev.next)
                prev = node
                # restore list link
                node.next = tmp
            i += 1
            node = node.next
        
        
        return res.next