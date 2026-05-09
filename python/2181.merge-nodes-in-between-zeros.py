# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        prev, cur = head, head.next

        while cur.next:
            if cur.val == 0:
                prev.next = cur
                prev = cur
            prev.val += cur.val
            cur = cur.next

        prev.next = None

        return head

