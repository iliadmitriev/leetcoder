class Solution:
    @staticmethod
    def sumOfDigits(n: int) -> int:
        s = 0
        while n:
            n, r = divmod(n, 10)
            s += r
        return s

    @staticmethod
    def sumMaxTwo(arr: list[int]) -> int:
        if len(arr) < 2:
            return -1

        max1, max2 = arr[0], arr[1]
        if max1 < max2:
            max1, max2 = max2, max1

        for i in range(2, len(arr)):
            if arr[i] > max1:
                max1, max2 = arr[i], max1
            elif arr[i] > max2:
                max2 = arr[i]
        return max1 + max2

    def maximumSum(self, nums: list[int]) -> int:
        maxPair = -1
        cache = {}

        for num in nums:
            cache.setdefault(self.sumOfDigits(num), []).append(num)

        for _, pair in cache.items():

            maxPair = max(maxPair, self.sumMaxTwo(pair))

        return maxPair

