from typing import Iterator, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(node: Optional[TreeNode]) -> Iterator[TreeNode]:
            if not node:
                return

            yield from inorder(node.left)
            yield node
            yield from inorder(node.right)

        def build_bst(nodes: list[TreeNode]) -> TreeNode:
            mid = len(nodes) // 2
            node = nodes[mid]

            if mid > 0:
                node.left = build_bst(nodes[:mid])
            else:
                node.left = None

            if mid < len(nodes) - 1:
                node.right = build_bst(nodes[mid + 1 :])
            else:
                node.right = None

            return node

        nodes = list(inorder(root))

        return build_bst(nodes)

