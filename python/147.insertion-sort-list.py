# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def insert_node(head, shead, stail):
            if shead == stail or head.val >= stail.val:
                stail.next = head
                head.next = None
                stail = head
            else:
                while shead.next and shead.next.val <= head.val:
                    shead = shead.next
                head.next = shead.next
                shead.next = head
            return stail

        
        shead = ListNode(None)
        stail = shead
        while head:
            temp = head.next
            stail = insert_node(head, shead, stail)
            head = temp
        return shead.next