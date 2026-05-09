import collections

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        def getLen(f: int) -> int:
            if f == 1:
                return 1
            if f < 10:
                return 2
            if f < 100:
                return 3
            return 4

        @cache
        def dp(i, k):
            if k < 0:
                return inf
            
            if i == len(s) or n - i <= k:
                return 0

            res = inf
            maxFreq = 0
            cnt = collections.Counter()

            for j in range(i, n):
                cnt.update(s[j])
                maxFreq = max(maxFreq, cnt.get(s[j]))

                res = min(
                    res,
                    getLen(maxFreq) + dp(j + 1, k - (j - i + 1 - maxFreq))
                )

            return res

        return dp(0, k)