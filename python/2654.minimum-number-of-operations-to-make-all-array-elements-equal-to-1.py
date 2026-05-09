

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)

        ones = nums.count(1)
        if ones > 0:
            return n - ones

        for d in range(2, n + 1):  # interval length
            for j in range(n - d + 1):
                g = gcd(nums[j], nums[j + 1])
                nums[j] = g

                if g == 1:
                    return d + n - 2

        return -1

