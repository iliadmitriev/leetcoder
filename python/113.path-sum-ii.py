

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res: list[list[int]] = []

        def dfs(node: TreeNode | None, path: list[int], target: int) -> None:
            if not node:
                return

            target -= node.val
            path.append(node.val)

            if not node.left and not node.right and target == 0:
                res.append(path.copy())

            dfs(node.left, path, target)
            dfs(node.right, path, target)
            _ = path.pop()

        dfs(root, [], targetSum)
        return res

