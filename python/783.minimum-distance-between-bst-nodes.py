# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        prev = float('-inf')
        res = float('inf')

        stack = [(root, False)]
        while stack:
            node, seen = stack.pop()
            if seen:
                res = min(res, node.val - prev)
                prev = node.val
            else:
                if node.right: stack.append((node.right, False))
                stack.append((node, True))
                if node.left: stack.append((node.left, False))
        
        return res