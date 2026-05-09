from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: TreeNode | None, depth: int = 0) -> tuple[TreeNode | None, int]:
            if not node:
                return None, depth

            left, d_left = dfs(node.left, depth + 1)
            right, d_right = dfs(node.right, depth + 1)

            if not left and not right:
                return node, depth

            if not left:
                return right, d_right

            if not right:
                return left, d_left

            if d_left == d_right:
                return node, d_left

            if d_left > d_right:
                return left, d_left

            return right, d_right

        node, _ = dfs(root)
        return node

