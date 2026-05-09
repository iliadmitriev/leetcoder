class Solution:
    def smallestNumber(self, pattern: str) -> str:

        def backtrack(i, p, used):
            if i == len(pattern) + 1:
                return p

            start, end = 1, 9

            if i > 0 and pattern[i - 1] == "I":
                start = int(p[i - 1]) + 1
            elif i > 0 and pattern[i - 1] == "D":
                end = int(p[i - 1]) - 1

            for j in range(start, end + 1):
                if used[j]:
                    continue

                used[j] = True
                res = backtrack(i + 1, p + str(j), used)
                used[j] = False

                if res:
                    return res

            return ""

        return backtrack(0, "", [False] * 10)
