class Solution:
    @staticmethod
    def sqrt(num: int, eps: float = 1e-6) -> float:
        """Sqrt using Newton's method."""
        x = num
        while abs(x * x - num) > eps:
            x = (x + num / x) / 2
        return x

    def isPerfectSquare(self, num: int) -> bool:
        return int(self.sqrt(num)) ** 2 == num

