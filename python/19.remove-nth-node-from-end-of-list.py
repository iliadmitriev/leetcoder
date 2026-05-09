# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # init pointer `last`
        # and move it forward n steps
        last = head
        while last and n:
            n -= 1
            last = last.next
            
        
        # init res and prev pointer as pointer to node before head node
        # init node as head node
        # mode forward both `last`  and `node` pointers simultaneously
        # util `last` pointer reaches the end
        # in this case `node` pointer will point to the n-th node from the end
        # and prev pointer will point to (n + 1)th node from the end
        res = ListNode()
        res.next, node, prev = head, head, res
        while last:
            prev = node
            node = node.next
            last = last.next
        
        # delete 
        prev.next = node.next
        return res.next
        