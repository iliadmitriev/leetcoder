class Solution:
    def minimumDeletions(self, s: str) -> int:
        """DP approach. Optimized.

        s:  a a b a b b a a b a b a a a b b b
        b:  0 0 1 1 2 3 3 3 4 4 5 5 5 5 6 7 8
        dp: 0 0 0 1 1 1 2 3 3 4 4 5 5 5 5 5 5
        """
        n = len(s)
        dp = 0
        b_count = 0
        for i in range(n):
            if s[i] == "b":
                b_count += 1
            else:
                dp = min(dp + 1, b_count)

        return dp

