class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @cache
        def dp(left, right):
            if left >= right:
                return 0

            return min(
                (right - left + dp(left, cut) + dp(cut, right) for cut in cuts if left < cut < right), default=0
            )

        return dp(0, n)
