class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        res = []

        i, j = 0, 0
        n = len(s)

        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1

            if j - i >= 3:
                res.append([i, j - 1])

            i = j

        return res

