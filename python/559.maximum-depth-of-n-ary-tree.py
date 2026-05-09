"""
# Definition for a Node.
"""


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0

        if not root.children:
            return 1

        return 1 + max(self.maxDepth(c) for c in root.children)

