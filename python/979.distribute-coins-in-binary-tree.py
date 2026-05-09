# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = [0]

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            """Returns size of subtree and total number of coins.

            Args:
                node: start node

            Returns:
                number of nodes.
                number of coins.
            """
            if not node:
                return 0, 0

            left_size, left_coins = dfs(node.left)
            right_size, right_coins = dfs(node.right)
            size = 1 + left_size + right_size
            coins = node.val + left_coins + right_coins

            res[0] += abs(size - coins)
            return size, coins

        dfs(root)

        return res[0]

