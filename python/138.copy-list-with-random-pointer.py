"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Time: O(n)
        Space: O(1)
        """
        if not head:
            return None

        # duplicate nodes in pairs:
        # original node 1 -> carbon copy 1 -> original node 2 -> carbon copy 2 -> ..
        ptr = head
        while ptr:
            ptr.next = Node(x=ptr.val, next=ptr.next)
            ptr = ptr.next.next

        # save pointer to head of carbon copy
        head_cc = head.next

        # set pointers to random nodes
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next

            ptr = ptr.next.next


        # recover original and carbon copy lists
        ptr, ptr_cc = head, head_cc
        while ptr_cc and ptr_cc.next:
            # split lists
            ptr.next = ptr.next.next
            ptr_cc.next = ptr_cc.next.next
            # move ahead
            ptr = ptr.next
            ptr_cc = ptr_cc.next

        # return saved pointer to head of carbon copy
        return head_cc
