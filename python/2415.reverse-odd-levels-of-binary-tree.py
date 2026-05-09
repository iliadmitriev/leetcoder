

class TreeNode:
    def __init__(
        self, val=0, left: "TreeNode | None" = None, right: "TreeNode | None" = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        def dfs(nodeLeft: TreeNode, nodeRight: TreeNode, level: int):

            if level % 2 == 1:
                nodeLeft.val, nodeRight.val = nodeRight.val, nodeLeft.val

            if nodeLeft.left and nodeRight.right:
                dfs(nodeLeft.left, nodeRight.right, level + 1)

            if nodeLeft.right and nodeRight.left:
                dfs(nodeLeft.right, nodeRight.left, level + 1)

        if root.left and root.right:
            dfs(root.left, root.right, 1)

        return root

