import math


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        power = math.ceil(math.log(n, 3))

        while n > 0:
            if n >= 3**power:
                n -= 3**power

            if n >= 3**power:
                return False

            power -= 1

        return True

