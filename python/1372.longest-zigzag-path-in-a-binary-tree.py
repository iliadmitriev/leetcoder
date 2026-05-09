# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        stack = [(root, 0, 0)]
        while stack:
            node, left, right = stack.pop()

            res = max(res, left, right)

            if node.right:
                stack.append((node.right, 0, left + 1))

            if node.left:
                stack.append((node.left, right + 1, 0))

        return res