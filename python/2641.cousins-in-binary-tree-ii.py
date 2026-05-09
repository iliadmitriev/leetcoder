
import operator
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root

        q = deque([(root, root.val)])

        level = 0
        n = operator.itemgetter(0)
        v = operator.attrgetter("val")

        while q:

            sumLevel = sum(map(v, map(n, q)))

            for _ in range(len(q)):
                node, brothers = q.popleft()

                node.val = sumLevel - brothers

                brothers = 0
                if node.left:
                    brothers += node.left.val
                if node.right:
                    brothers += node.right.val

                if node.left:
                    q.append((node.left, brothers))

                if node.right:
                    q.append((node.right, brothers))

            level += 1

        return root


