# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode | None, val: int) -> int:
            if node is None:
                return 0

            cur = (val << 1) + node.val

            if node.left is None and node.right is None:
                return cur

            return dfs(node.left, cur) + dfs(node.right, cur)

        return dfs(root, 0)
            