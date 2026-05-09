from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        q = deque([root])
        levels = []

        while q:

            maxVal = q[0].val

            for _ in range(len(q)):
                node = q.popleft()

                if node.val > maxVal:
                    maxVal = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levels.append(maxVal)

        return levels

