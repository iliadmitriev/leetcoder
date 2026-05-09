class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inorder = [0] * (n + 1)

        for u, v in trust:
            inorder[u] -= 1
            inorder[v] += 1

        for i in range(1, n + 1):
            if inorder[i] == n - 1:
                return i

        return -1

