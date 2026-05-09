# Definition for a binary tree node.
class Solution:
    def delNodes(self, root: TreeNode | None, to_delete: list[int]) -> list[TreeNode]:
        if not root:
            return []

        toDelete = set(to_delete)
        result: list[TreeNode] = []

        def dfs(
            node: TreeNode | None,
            is_root: bool,
        ) -> TreeNode | None:
            if not node:
                return None

            if is_root and node.val not in toDelete:
                result.append(node)

            node.left = dfs(node.left, node.val in toDelete)
            node.right = dfs(node.right, node.val in toDelete)

            return node if node.val not in toDelete else None

        _ = dfs(root, root.val not in toDelete)
        return result

