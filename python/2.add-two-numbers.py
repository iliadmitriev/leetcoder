# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = ''
        while l1:
            d1 = str(l1.val) + d1
            l1 = l1.next
            
        d2 = ''
        while l2:
            d2 = str(l2.val) + d2
            l2 = l2.next
            
        res = int(d1) + int(d2)
        
        head = curr = ListNode(-1)
        for ch in str(res)[::-1]:
            curr.next = ListNode(int(ch))
            curr = curr.next
            
        return head.next