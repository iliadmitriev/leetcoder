class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        res = 0
        n = len(arr)

        # convolution k * (n - k - 1)  k => 1..n

        for i, num in enumerate(arr):
            res += ((i + 1) * (n - i) + 1) // 2 * num

        return res

