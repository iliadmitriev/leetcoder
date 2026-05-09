# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1. find the middle
        2. split the list in two
        3. reverse the second part
        4. merge lists

        modify head in place
        """
        if not head or not head.next:
            return

        # find the middle
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the list in two
        if not slow:
            return

        mid, slow.next = slow.next, None

        # reverse the second part
        cur, pre = mid, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        # merge lists
        a, b = head, pre
        while a and b:
            aa, bb = a, b
            a, b = a.next, b.next
            aa.next, bb.next = bb, a

