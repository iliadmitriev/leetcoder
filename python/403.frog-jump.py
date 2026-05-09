class Solution:
    def canCross(self, stones: List[int]) -> bool:
        last = stones[-1]
        stones_set = set(stones)

        @cache
        def dp(i: int, k: int) -> bool:
            if k == 0:
                return False

            if i == last:
                return True

            if i + k not in stones_set:
                return False

            res = False

            for j in (-1, 0, 1):
                if dp(i + k, k + j):
                    res = True
                    break

            return res

        return dp(0, 1)