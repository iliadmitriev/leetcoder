# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        
        while node:
            
            # if previous and current node has equal values
            # then reassing link (throw away current node)
            if prev and prev.val == node.val:
                prev.next = node.next
            else:
                # otherwise move foraward previous node
                prev = node
            
            # move forawrd
            node = node.next
                
        return head