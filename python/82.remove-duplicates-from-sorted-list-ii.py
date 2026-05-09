# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = prev = ListNode(0, head)
        ptr = head
        
        while ptr:
            # if there is a duplicate
            if ptr.next and ptr.val == ptr.next.val:
                # fast forward ptr till the end of duplicates
                while ptr.next and ptr.val == ptr.next.val:
                    # move pointer to next item
                    ptr = ptr.next
                # skip all duplicates
                prev.next = ptr.next
            else:
                # one step forward prev pointer
                prev = prev.next
            
            # ptr one step forward
            ptr = ptr.next
                
        return res.next