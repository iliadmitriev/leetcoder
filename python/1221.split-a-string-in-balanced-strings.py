class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0

        for c in s:
            balance += 1 - 2 * (c == "L")
            count += 1 * (balance == 0)

        return count

