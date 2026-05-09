# Definition for a binary tree node.
from collections.abc import Iterator
from typing import Self


class TreeNode:
    def __init__(
        self, val: int = 0, left: Self | None = None, right: Self | None = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:

        def postorder(node: TreeNode | None) -> Iterator[int]:
            if not node:
                return

            yield from postorder(node.left)
            yield from postorder(node.right)
            yield node.val

        return list(postorder(root))

