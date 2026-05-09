# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # if list is empty or has only one node
        if not head or not head.next:
            return True

        # find the middle, and reverse left part
        slow, fast, prev = head, head, None
        while slow and fast and fast.next:
            tmp = slow

            slow = slow.next
            fast = fast.next.next

            tmp.next = prev
            prev = tmp

        # if nodes count is odd, skip the middle node
        if fast and slow:
            slow = slow.next

        # compare
        while prev and slow and prev.val == slow.val:
            slow = slow.next
            prev = prev.next

        # if reached last, return True
        return not prev

