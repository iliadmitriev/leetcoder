# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Idea: Inorder traverse BST, compare current node value with previous.
              Find ninimum difference.
        """
        if not root:
            return 0

        stack = deque([(root, False)])
        prev = -float("inf")
        res = float("inf")
        while stack:
            node, process = stack.pop()
            if process:
                res = min(res, node.val - prev)
                prev = node.val
            else:
                if node.right: stack.append((node.right, False))
                stack.append((node, True))
                if node.left: stack.append((node.left, False))
        return res
