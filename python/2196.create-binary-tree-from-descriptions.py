

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        if not descriptions:
            return None

        root: TreeNode | None = None
        tree: dict[int, TreeNode] = {}
        hasParent: set[int] = set()

        for parent, child, isLeft in descriptions:
            hasParent.add(child)

            if parent not in tree:
                tree[parent] = TreeNode(parent)
            if child not in tree:
                tree[child] = TreeNode(child)

            if isLeft:
                tree[parent].left = tree[child]
            else:
                tree[parent].right = tree[child]

        for parent, *_ in descriptions:
            if parent not in hasParent:
                root = tree[parent]

        return root

