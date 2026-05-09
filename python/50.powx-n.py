class Solution:
    def myPow(self, x: float, n: int) -> float:

        def bin_pow(x: float, n: int) -> float:
            if n == 0:
                return 1.0
            elif n < 0:
                return 1.0 / bin_pow(x, -n)
        
            if n % 2:
                return x * bin_pow(x * x, (n - 1) / 2)
            else:
                return bin_pow(x * x, n / 2)

        return bin_pow(x, n)