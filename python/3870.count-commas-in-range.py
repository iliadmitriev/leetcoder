class Solution:
    def countCommas(self, n: int) -> int:
        if 10**6 > n >= 10**6:
            return (n - 10**6 + 1) + self.countCommas(10**6 - 1)
        elif n >= 10**3:
            return (n - 10**3 + 1) + self.countCommas(10**3 - 1)

        return 0


        