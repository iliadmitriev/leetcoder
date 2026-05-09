class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Multiply strings as big numbers
        (using classic elementary math multiplication approach)

        :param num1: string containing first number of length m
        :param num2: string containing second number of length n
        :return: string representing multiplication of num1 and num2
        """
        # get m, n - lengths of num1 and num2 respectively
        m, n = map(len, [num1, num2])
        # array of int to store result of multiplication
        prod = [0] * (m + n)
        # a - runs through all digits in first num1
        #     starting from last to first symbol of a string
        #     from lowest to highest digit
        # i - 0 .. m - 1
        for i, a in enumerate(reversed(num1)):
            # b - last to first symbol of num2 (lowest to highest digit)
            # j - 0 .. n - 1
            for j, b in enumerate(reversed(num2)):
                # accumulate to i + j position of result digits `a` and `b`
                prod[i + j] += int(a) * int(b)
                # accumulate multiplication carry to next higher order digit
                prod[i + j + 1] += prod[i + j] // 10
                # left the remainder in lowest order digit
                prod[i + j] %= 10
        # built result joining reversed array of digits converted to string
        # removing leading zeroes
        res = (''.join(map(str, reversed(prod)))).lstrip('0')
        # return result if it's not empty, otherwise return '0'
        return res if res else '0'
