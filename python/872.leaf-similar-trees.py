# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            st = [root]
            while st:
                node = st.pop()

                if not node.left and not node.right:
                    yield node.val

                if node.right:
                    st.append(node.right)

                if node.left:
                    st.append(node.left)

        it1, it2 = dfs(root1), dfs(root2)

        while True:
            v1, v2 = next(it1, None), next(it2, None)

            if v1 != v2:
                return False

            if v1 is None and v2 is None:
                return True

        return False
