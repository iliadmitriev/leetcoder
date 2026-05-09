# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        last, first, second = res, res, res
        while last and k:
            last = last.next
            k -= 1
            
        second, first = res, last
        while last:
            second = second.next
            last = last.next
            
        first.val, second.val = second.val, first.val
        return res.next