# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root: TreeNode, total: int) -> int:
        if not root:
            return 0
        total = total * 10 + root.val

        if not root.left and not root.right:
            return total

        res = 0
        if root.left:
            res += self.dfs(root.left, total)
        if root.right:
            res += self.dfs(root.right, total)

        return res

    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return self.dfs(root, 0)

