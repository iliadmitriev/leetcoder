# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, root.val, root.val)])
        res = 0
        
        while queue:
            node, lo, hi = queue.pop()

            if not node:
                res = max(res, hi - lo)
                continue

            lo = min(lo, node.val)
            hi = max(hi, node.val)

            queue.append((node.right, lo, hi))
            queue.append((node.left, lo, hi))
                
        return res

