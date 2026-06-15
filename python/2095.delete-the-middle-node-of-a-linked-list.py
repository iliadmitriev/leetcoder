# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        prev, mid, end = None, head, head

        while end and end.next:
            prev = mid
            mid = mid.next
            end = end.next.next

        if not prev:
            return None

        if mid:
            prev.next = mid.next

        return head
        