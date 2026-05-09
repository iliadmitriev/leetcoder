class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def isSelfDividing(n: int) -> bool:
            x = n

            while x:
                x, d = divmod(x, 10)
                if d == 0 or n % d != 0:
                    return False

            return True

        return [n for n in range(left, right + 1) if isSelfDividing(n)]

