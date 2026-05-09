# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def smallest(node: TreeNode, path: str) -> str:
            if not node.left and not node.right:
                return chr(node.val + 97) + path

            res = []
            if node.left:
                res.append(smallest(node.left, chr(node.val + 97) + path))

            if node.right:
                res.append(smallest(node.right, chr(node.val + 97) + path))

            return min(res)

        if not root:
            return ""

        return smallest(root, "")

