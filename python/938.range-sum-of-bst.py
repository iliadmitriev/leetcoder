# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def inorder(node, low, high):
            if low <= node.val <= high:
                yield node.val

            if low <= node.val and node.left:
                yield from inorder(node.left, low, high)

            if node.val <= high and node.right:
                yield from inorder(node.right, low, high)

        return sum(inorder(root, low, high)) if root else 0