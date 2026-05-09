# Definition for a binary tree node.
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        assert root
        assert root.left
        assert root.right

        return root.val == root.left.val + root.right.val

