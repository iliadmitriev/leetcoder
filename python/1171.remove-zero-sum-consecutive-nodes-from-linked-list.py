# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        cur = head
        prefix = 0
        pre = [0]
        cache = {0: dummy}
        while cur:
            prefix += cur.val
            if prefix not in cache:
                cache[prefix] = cur
                pre.append(prefix)
            else:
                prev = cache[prefix]
                while pre and pre[-1] != prefix:
                    cache.pop(pre.pop())
                prev.next = cur.next
            cur = cur.next

        return dummy.next

