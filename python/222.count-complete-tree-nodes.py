# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node: TreeNode, direction: str) -> int:
        res = 0
        while node:
            node = getattr(node, direction)
            res += 1
        return res

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.height(root, 'left')
        right_height = self.height(root, 'right')

        if left_height == right_height:
            return 2**left_height - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)