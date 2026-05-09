"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        recursive bfs
        a) check if root is exist
        b) check if left child of root is exist 
           than set it next to the right child
        c) check if right child of root is exist
           and root has next link
           than set rigth child next link to the 
           leftmost child of root's next
        d) recurse for left and right children of root
                 
                  1  --> x
                /    \
              /        \
             2   -->    3  --> x
           /   \      /   \
          4 --> 5 -> 6 --> 7 --> x
             b    c  
            
        """
        if not root:
            return root
        
        if root and root.left:
            root.left.next = root.right
        
        if root and root.right and root.next:
            root.right.next = root.next.left
            
        self.connect(root.left)
        self.connect(root.right)
        
        return root