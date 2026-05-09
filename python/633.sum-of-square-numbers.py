from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # fermat theorem all prime factors of given number
        # which can be represented as 4 * i + 3, should not occur odd

        for i in range(2, int(sqrt(c)) + 1):

            if c % i:
                continue

            cnt = 0
            while c % i == 0:
                cnt += 1
                c //= i

            if i % 4 == 3 and cnt % 2 == 1:
                return False

        return c % 4 != 3

