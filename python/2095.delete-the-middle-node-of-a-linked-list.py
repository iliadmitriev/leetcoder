# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        res.next = head
        step1x = step2x = res
        
        # step 2x pointer forward to get one node before middle node
        step2x = step2x.next
        
        # find middle
        while step2x and step2x.next:
            step1x = step1x.next
            step2x = step2x.next.next
        
        # remove middle by crosslinking
        step1x.next = step1x.next.next
        return res.next