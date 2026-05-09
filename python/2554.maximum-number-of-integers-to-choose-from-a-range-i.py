class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        total, count = 0, 0

        bannedCache = set(banned)

        for i in range(1, n + 1):
            if i in bannedCache:
                i += 1
                continue

            if i + total <= maxSum:
                total += i
                count += 1
            else:
                break

        return count

