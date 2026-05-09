# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """Find a common node for two linked lists.
        
        Single space solution.
        
        Algorithm:
        
        1. iterate both lists to find their length
        2. find difference
        3. iterate longer list to make tails of lists of the same length
        4. iterate both lists while their nodes don't match
           (while same node is not found)
           
                       a1 -> a2
                                \ 
                                  c1 -> c2 -> c2
                                /
           b1 -> b2 -> b3 -> b4
           
        """
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a
        