from math import isqrt

class Solution:
    def numSquares(self, n: int) -> int:
        # case 1: check if number is already a square
        if isqrt(n) ** 2 == n:
            return 1

        # case 2: check if number can be split to sum of two squares
        for i in range(1, isqrt(n) + 1):
            x = n - i**2
            if x == isqrt(x)**2:
                return 2

        # case 3: check if number consist of 3 numbers (Lagrange's theoreme of sum of three squares)
        while n%4 == 0: n //= 4
        if n % 8 != 7: return 3

        # case 4: Lagrange's theoreme any natural number can be repsesented as of sum of 4 squares
        return 4