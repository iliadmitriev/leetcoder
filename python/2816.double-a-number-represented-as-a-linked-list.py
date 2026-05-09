# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head

        if head.val > 4:
            head = ListNode(1, head)

        while cur.next:
            cur.val = (cur.val * 2 + cur.next.val // 5) % 10
            cur = cur.next

        cur.val = (cur.val * 2) % 10

        return head

