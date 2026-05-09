

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: TreeNode | None) -> int:
        nodeSum = []
        MOD = int(1e9) + 7

        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            res = node.val + left + right
            nodeSum.append(res)

            return res

        dfs(root)

        total = nodeSum.pop()

        return max(v * (total - v) for v in nodeSum) % MOD

