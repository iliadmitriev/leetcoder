class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        res = 0

        mid, end = head, head

        stack = []

        while end and end.next:
            stack.append(mid.val)
            mid = mid.next
            end = end.next.next

        while mid and stack:
            v1, v2 = mid.val, stack.pop()
            res = max(res, v1 + v2)

            mid = mid.next

        return res
