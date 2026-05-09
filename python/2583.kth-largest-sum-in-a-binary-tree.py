from collections import deque


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: TreeNode | None, k: int) -> int:
        if not root:
            return 0

        levels = []

        que = deque([root])

        while que:
            levelSum = 0
            for _ in range(len(que)):
                node = que.popleft()
                levelSum += node.val

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            levels.append(levelSum)

        levels.sort(reverse=True)

        if len(levels) < k:
            return -1

        return levels[k - 1]

