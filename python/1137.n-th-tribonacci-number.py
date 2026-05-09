class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        res = 0
        t_0 = 0
        t_1 = 1
        t_2 = 1

        for _ in range(2, n):
            res = t_0 + t_1 + t_2
            t_0 = t_1
            t_1 = t_2
            t_2 = res

        return res

