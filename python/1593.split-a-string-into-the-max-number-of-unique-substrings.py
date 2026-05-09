class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        cache: set[str] = set()

        def backtrack(cache: set[str], i: int) -> int:
            if i == len(s):
                return len(cache)

            result = 0

            for j in range(i, len(s)):
                if s[i: j + 1] in cache:
                    continue
                cache.add(s[i: j + 1])
                result = max(result, backtrack(cache, j + 1))
                cache.remove(s[i: j + 1])

            return result

        return backtrack(cache, 0)

