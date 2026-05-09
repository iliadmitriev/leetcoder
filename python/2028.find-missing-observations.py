class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:

        m = len(rolls)
        total = mean * (m + n)

        total -= sum(rolls)

        if total < n or total > n * 6:
            return []

        return [total // n] * (n - total % n) + [total // n + 1] * (total % n)

