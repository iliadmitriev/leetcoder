class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = []

        while n:
            n, d = divmod(n, 10)

            if d != 0:
                nums.append(d)

        x = 0
        s = 0

        while nums:
            d = nums.pop()
            x *= 10
            x += d
            s += d

        return x * s
