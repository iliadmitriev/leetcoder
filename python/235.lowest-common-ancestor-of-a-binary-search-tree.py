# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lo, hi = (p, q) if p.val < q.val else (q, p)

        while root:
            if lo.val <= root.val <= hi.val:
                return root
            if root.val < lo.val:
                root = root.right
            elif root.val > hi.val:
                root = root.left
        return root
