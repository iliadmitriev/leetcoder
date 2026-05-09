class Solution:
    def constructFromPrePost(
        self, preorder: list[int], postorder: list[int]
    ) -> TreeNode | None:
        st: list[TreeNode] = []
        i, j = 0, 0
        n = len(preorder)

        node = None

        while j < n:
            if st and st[-1].val == postorder[j]:
                node = st.pop()
                j += 1
                continue

            node = TreeNode(preorder[i])
            i += 1

            if st:
                if st[-1].left is None:
                    st[-1].left = node
                else:
                    st[-1].right = node

            st.append(node)

        return node

