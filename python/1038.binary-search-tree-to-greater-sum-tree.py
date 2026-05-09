# Definition for a binary tree node.
from collections import deque


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0

        st: deque[tuple[TreeNode, bool]] = deque()
        st.append((root, False))

        while st:
            node, done = st.pop()

            if done:
                total += node.val
                node.val = total
                continue

            if node.left:
                st.append((node.left, False))

            st.append((node, True))

            if node.right:
                st.append((node.right, False))

        return root

