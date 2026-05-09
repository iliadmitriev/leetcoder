# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, mid, prev = slow, slow, None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        first, second = head, prev

        max_sum = 0
        while first and second:
            max_sum = max(max_sum, first.val + second.val)
            first, second = first.next, second.next

        return max_sum
