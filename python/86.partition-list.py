# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less, rest = ListNode(None), ListNode(None)
        less_head, rest_head = less, rest

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                rest.next = head
                rest = rest.next
            
            head = head.next

        less.next = rest_head.next
        rest.next = None
        return less_head.next