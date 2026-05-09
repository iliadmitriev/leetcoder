class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = [[] for _ in range(len(parent))]
        for i, p in enumerate(parent):
            if p != -1:
                children[p].append(i)

        def dfs(children, node, s, res):

            first_max_chain, second_max_chain = 0, 0

            for child in children[node]:
                curr, res = dfs(children, child, s, res)

                if s[child] == s[node]:
                    continue

                if first_max_chain < curr:
                    second_max_chain = first_max_chain
                    first_max_chain = curr
                elif second_max_chain < curr:
                    second_max_chain = curr

            res = max(res, 1 + first_max_chain + second_max_chain)
            return 1 + first_max_chain, res

        _, res = dfs(children, 0, s, 1)

        return res