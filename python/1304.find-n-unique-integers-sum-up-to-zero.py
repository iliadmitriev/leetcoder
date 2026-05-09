class Solution:
    def sumZero(self, n: int) -> list[int]:
        res: list[int] = []

        if n % 2:
            res.append(0)

        for x in range(1, n // 2 + 1):
            res.append(x)
            res.append(-x)

        return res

