# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1. Init (prev and current):
      p    c    
    res -> 1 -> 2 -> 3 -> 4 -> 5 -> x

    1. save pointer to next pair

      p    c         n
    res -> 1 -> 2 -> 3 -> 4 -> 5 -> x

    2. get second pointer for swapping

      p    c    s    n
    res -> 1 -> 2 -> 3 -> 4 -> 5 -> x

    3. swap pointers
      - prev pointer to second node:
         c    s    n
         1 -> 2 -> 3 -> 4 -> 5 -> x
             /
          res, p

      - second node to current node
         c <- s    n
         1 -> 2    3 -> 4 -> 5 -> x
             /
          res, p

      - current node to next pair node
           ______
          /      \
         c    s    n
         1 <- 2    3 -> 4 -> 5 -> x
             /
          res, p
 
        OR (current and secod nodes swapped)
 
          p    s    c    n
        res -> 2 -> 1 -> 3 -> 4 -> 5 -> x

      4. move forward:
          previous pointer to current
          current pointer to next pair pointer
                    p    c
        res -> 2 -> 1 -> 3 -> 4 -> 5 -> x

    

    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
          return head

        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head

        return second

