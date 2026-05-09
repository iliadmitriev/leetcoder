# Definition for a Node.
# class Node:
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child

class Solution:
    def flatten_recursive(self, head):
        node = head
        tail = node
        while node:
            if node.child:
                child_head, child_tail = self.flatten_recursive(node.child)
                tmp = node.next
                node.next = child_head
                child_head.prev = node
                if tmp:
                    child_tail.next = tmp
                    tmp.prev = child_tail
                node.child = None
                node = child_tail

            tail = node
            node = node.next

        return head, tail

    
    def flatten(self, head):
        head, _ = self.flatten_recursive(head)
        return head
