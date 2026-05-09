# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, val, depth, cur_depth):
        if not root:
            return None

        if cur_depth == depth - 1:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
            return root
        if cur_depth < depth:
            root.left = self.dfs(root.left, val, depth, cur_depth + 1)
            root.right = self.dfs(root.right, val, depth, cur_depth + 1)

        return root

    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:

        if depth == 1:
            return TreeNode(val, root, None)

        return self.dfs(root, val, depth, 1)

