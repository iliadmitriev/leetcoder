from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def treeQueries(self, root: TreeNode | None, queries: list[int]) -> list[int]:

        maxHeight = defaultdict(int)
        currentMaxHeight = 0

        def postorder(
            node: TreeNode | None,
            curHeight: int,
            maxHeight: dict[int, int],
            left: bool = True,
        ):
            if not node:
                return

            nonlocal currentMaxHeight

            maxHeight[node.val] = max(maxHeight[node.val], currentMaxHeight)
            currentMaxHeight = max(currentMaxHeight, curHeight)

            if left:
                postorder(node.left, curHeight + 1, maxHeight, left)
                postorder(node.right, curHeight + 1, maxHeight, left)
            else:
                postorder(node.right, curHeight + 1, maxHeight, left)
                postorder(node.left, curHeight + 1, maxHeight, left)

        postorder(root, 0, maxHeight, True)
        currentMaxHeight = 0
        postorder(root, 0, maxHeight, False)

        return [maxHeight[q] for q in queries]

