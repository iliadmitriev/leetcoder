# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def comp(a, b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return True
            return False
        
        deq = deque([(p, q),])
        
        while deq:
            p, q = deq.popleft()
            
            if not comp(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                
        return True
        