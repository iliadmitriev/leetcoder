# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # init false start
        start = ListNode(next=head)

        # init previous and current pointers
        pre = start
        cur = start.next

        # find left pointer
        for _ in range(1, left):
            pre = cur
            cur = cur.next

        # reverse
        for _ in range(right - left):
            # set temp pointer next after current
            tmp = cur.next
            # link current to next after temp
            cur.next = tmp.next
            # link temp to next after previous
            tmp.next = pre.next
            # link previous to temp
            pre.next = tmp
        
        # return next after false start
        return start.next