# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def helper(preorder: list[int], hi: int) -> Optional[TreeNode]:
            if not preorder or preorder[0] > hi:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            root.left = helper(preorder, val)
            root.right = helper(preorder, hi)
            return root

        return helper(preorder, 10**9)

