# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumLeftLeaves(self, node: Optional[TreeNode], isLeft: bool) -> int:
        if not node:
            return 0
        if isLeft and not node.left and not node.right:
            return node.val
        return self.sumLeftLeaves(node.left, True) + self.sumLeftLeaves(
            node.right, False
        )

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.sumLeftLeaves(root, False)

