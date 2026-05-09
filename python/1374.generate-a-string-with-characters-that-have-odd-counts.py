class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return "a" * n

        a = 1
        b = n - 1

        return a * "a" + b * "b"

