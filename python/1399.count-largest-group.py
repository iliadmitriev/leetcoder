

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sumDigits(n: int) -> int:
            res = 0
            while n:
                n, r = divmod(n, 10)
                res += r

            return res

        d = [0] * (sumDigits(10**4 - 1) + 1)

        for i in range(1, n + 1):
            key = sumDigits(i)
            d[key] += 1

        largestSize = 0
        largest = 0

        for cnt in d:
            if cnt > largest:
                largest = cnt
                largestSize = 1

            elif cnt == largest:
                largestSize += 1

        return largestSize

