# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        o    e 
        1 -> x 

        o    e
        1 -> 2 -> x

               2
             o  \ e
             3 -> 4 -> 5 -> x
            /
         1 

        """
        if not head:
            return None

        odd = head
        even = odd.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head