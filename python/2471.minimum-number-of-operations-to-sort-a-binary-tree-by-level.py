from collections import deque


class TreeNode:
    def __init__(
        self, val=0, left: "TreeNode | None" = None, right: "TreeNode | None" = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        q = deque([root])
        swaps = 0

        while q:

            level = []

            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            swaps += self._get_swaps(level)

        return swaps

    def _get_swaps(self, original: list[int]):
        swaps = 0
        target = sorted(original)
        pos = {v: i for i, v in enumerate(original)}

        for i in range(len(original)):
            if original[i] != target[i]:
                swaps += 1
                cur = pos[target[i]]
                pos[original[i]] = cur
                original[cur] = original[i]

        return swaps

