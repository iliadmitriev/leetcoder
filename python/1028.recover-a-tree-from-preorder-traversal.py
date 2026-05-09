

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:

        def dfs(traversal: str, i: int, depth: int) -> tuple[TreeNode | None, int]:
            if i >= len(traversal):
                return None, i

            j = i
            while j < len(traversal) and traversal[j] == "-":
                j += 1

            if j - i < depth:
                return None, i

            k = j
            while k < len(traversal) and traversal[k].isdigit():
                k += 1

            val = int(traversal[j:k])
            node = TreeNode(val)

            node.left, p = dfs(traversal, k, depth + 1)
            node.right, m = dfs(traversal, p, depth + 1)

            return node, m

        return dfs(traversal, 0, 0)[0]

