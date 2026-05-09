

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node: TreeNode | None, depth: int) -> tuple[TreeNode | None, int]:
        if not node:
            return None, 0

        left, left_depth = self.dfs(node.left, depth + 1)
        right, right_depth = self.dfs(node.right, depth + 1)

        if not left and not right:
            return node, depth
        elif left_depth > right_depth:
            return left, left_depth
        elif right_depth > left_depth:
            return right, right_depth

        return node, left_depth

    def subtreeWithAllDeepest(self, root: TreeNode | None) -> TreeNode | None:
        node, _ = self.dfs(root, 0)
        return node

