# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Idea:
        Main idea is to use Floyd's Cycle detection:
        https://en.wikipedia.org/wiki/Cycle_detection
        Use two pointers (fast and slow).
        For one step of slow pointer, fast pointer makes two steps.
        If there's cycle pointers will meet.
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # look for a start node of cycle
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
            
        return None
        