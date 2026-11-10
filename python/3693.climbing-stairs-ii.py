class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        f, f1, f2 = 0, 0, 0

        for cost in costs:
            f, f1, f2 = cost + min(f + 1, f1 + 4, f2 + 9), f, f1

        return f
