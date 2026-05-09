# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next:
            return [-1, -1]

        firstIdx = -1
        prevIdx = -1

        minDistance = -1
        maxDistance = -1

        prev = head
        curr = head.next
        i = 1

        while curr and curr.next:
            if (prev.val < curr.val and curr.val > curr.next.val) or (
                prev.val > curr.val and curr.val < curr.next.val
            ):

                if firstIdx != -1:
                    maxDistance = i - firstIdx
                    if minDistance == -1:
                        minDistance = i - prevIdx
                    minDistance = min(minDistance, i - prevIdx)
                else:
                    firstIdx = i

                prevIdx = i

            prev = curr
            curr = curr.next
            i += 1

        return [minDistance, maxDistance]

