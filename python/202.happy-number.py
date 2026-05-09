class Solution:
    def isHappy(self, n: int) -> bool:
        s = {n}
        while n != 1:
            n2 = 0
            while n:
                n, x = divmod(n, 10)
                n2 += x**2

            n = n2
            if n in s:
                return False

            s.add(n)

        return True

