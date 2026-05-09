# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        inf = 2**32 - 1
        first, second = inf, inf

        q = deque([root])
        while q:

            node = q.popleft()
            if first > node.val:
                first, second = node.val, first
            elif second > node.val and node.val != first:
                second = node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        if second == inf:
            return -1
        return second

