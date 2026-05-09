

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if limit * 3 < n:
            return 0
        elif limit * 3 == n:
            return 1

        total = 0

        lower = max(0, n - limit * 2)
        upper = min(n, limit)

        for a in range(lower, upper + 1):
            remain = n - a
            if remain < 0:
                continue

            lower_b = max(0, remain - limit)
            upper_b = min(remain, limit)

            if lower_b <= upper_b:
                total += upper_b - lower_b + 1

        return total

