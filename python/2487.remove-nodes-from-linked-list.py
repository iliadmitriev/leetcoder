# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseLinkedList(head)

        cur = head
        while cur:
            if cur.next and cur.val > cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return self.reverseLinkedList(head)

