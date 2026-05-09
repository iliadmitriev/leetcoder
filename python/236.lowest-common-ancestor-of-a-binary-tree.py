

class Solution:
    def getPath(
        self, node: TreeNode | None, target: TreeNode, path: list[TreeNode]
    ) -> bool:
        if not node:
            return False

        if (
            node == target
            or self.getPath(node.left, target, path)
            or self.getPath(node.right, target, path)
        ):
            path.append(node)
            return True

        return False

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        pPath: list[TreeNode] = []
        qPath: list[TreeNode] = []
        _ = self.getPath(root, p, pPath)
        _ = self.getPath(root, q, qPath)

        res: TreeNode = root
        while pPath and qPath and pPath[-1] == qPath[-1]:
            res = pPath[-1]
            _ = qPath.pop()
            _ = pPath.pop()

        return res

