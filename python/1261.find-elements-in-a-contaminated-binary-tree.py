class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: TreeNode | None):
        self.root = root
        self.nodes = set()
        self._recover(self.root, 0)

    def _recover(self, root: TreeNode | None, val: int):
        if not root:
            return

        self.nodes.add(val)

        self._recover(root.left, 2 * val + 1)
        self._recover(root.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.nodes

