# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        node = head
        while node:
            prev = node
            node = node.next

            while node and node.val == val:
                node = node.next

            prev.next = node

        return head
