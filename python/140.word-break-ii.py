from functools import partial
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        words = set(wordDict)
        maxLen = len(s)

        def dfs(i: int, cur: list[str]) -> None:
            if i == len(s):
                res.append(cur.copy())
                return

            if i > len(s):
                return

            for j in range(i, maxLen):
                if s[i: j + 1] in words:
                    cur.append(s[i: j + 1])
                    dfs(j + 1, cur)
                    cur.pop()

        dfs(0, [])
        join_space = partial(str.join, " ")
        return list(map(join_space, res))

