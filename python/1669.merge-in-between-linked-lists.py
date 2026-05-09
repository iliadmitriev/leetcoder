# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        tail = list2
        while tail and tail.next:
            tail = tail.next

        cur = list1
        for _ in range(a - 1):
            cur = cur.next
        first = cur

        for _ in range(b - a + 2):
            cur = cur.next
        second = cur

        first.next = list2
        tail.next = second

        return list1

