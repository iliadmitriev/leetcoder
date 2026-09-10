# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode | None) -> int:
        res = [0]

        def dfs(node: TreeNode | None) -> tuple[int, int]:  # sum, count
            if not node:
                return 0, 0

            leftSum, leftCount = dfs(node.left)
            rightSum, rightCount = dfs(node.right)

            total = leftSum + rightSum + node.val
            count = leftCount + rightCount + 1

            if (total // count) == node.val:
                res[0] += 1

            return total, count

        dfs(root)

        return res[0]
