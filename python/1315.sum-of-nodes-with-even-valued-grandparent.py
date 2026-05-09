# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        q: deque[tuple[TreeNode, Optional[TreeNode], Optional[TreeNode]]] = deque(
            [(root, None, None)]
        )
        while q:
            node, parent, grand_parent = q.popleft()

            if grand_parent and grand_parent.val % 2 == 0:
                res += node.val
            if node.left:
                q.append((node.left, node, parent))
            if node.right:
                q.append((node.right, node, parent))

        return res

