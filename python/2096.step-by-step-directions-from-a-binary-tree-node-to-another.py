

class Solution:
    def getPathForNode(self, root: TreeNode | None, val: int, path: list[str]) -> bool:
        if not root:
            return False

        if root.val == val:
            return True

        if self.getPathForNode(root.left, val, path):
            path.append("L")
            return True

        if self.getPathForNode(root.right, val, path):
            path.append("R")
            return True

        return False

    def getDirections(
        self, root: TreeNode | None, startValue: int, destValue: int
    ) -> str:

        startPath: list[str] = []
        _ = self.getPathForNode(root, startValue, startPath)

        destPath: list[str] = []
        _ = self.getPathForNode(root, destValue, destPath)

        while startPath and destPath and startPath[-1] == destPath[-1]:
            _ = startPath.pop()
            _ = destPath.pop()

        return "".join(["U"] * (len(startPath)) + destPath[::-1])

