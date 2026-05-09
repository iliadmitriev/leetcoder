# Definition for singly-linked list.
from collections import defaultdict, deque
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        if not head:
            return 0

        prev, head = head, head.next
        to_visit = set(nums)
        res = len(nums)

        while head:
            if prev.val in to_visit and head.val in to_visit:
                res -= 1

            prev, head = head, head.next

        return res

