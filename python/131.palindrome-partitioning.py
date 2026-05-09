from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:

        def pal(s: str, i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(s: str, i: int, path: List[str], res: List[List[str]]):
            if i >= len(s):
                res.append(path.copy())
                return

            for j in range(i + 1, len(s) + 1):
                if pal(s, i, j - 1):
                    path.append(s[i:j])
                    dfs(s, j, path, res)
                    path.pop()

        res: list[list[str]] = []
        dfs(s, 0, [], res)
        return res

