class Solution:
    @staticmethod
    def rev(x: int) -> int:
        r = 0
        while x:
            r = r * 10 + x % 10
            x //= 10

        return r

    def mirrorDistance(self, n: int) -> int:
        return abs(n - self.rev(n))

