class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count(x: int) -> int:
            if x < 100:
                return 0

            c = 0
            x, r2 = divmod(x, 10)
            x, r1 = divmod(x, 10)
            
            while x > 0:
                x, r = divmod(x, 10)

                if r2 > r1 < r or r2 < r1 > r:
                    c += 1
                    
                r2, r1 = r1, r

            return c

        res = 0
        for x in range(num1, num2 + 1):
            res += count(x)

        return res

