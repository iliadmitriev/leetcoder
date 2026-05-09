class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        if total < p:
            return -1

        rem = total % p
        if rem == 0:
            return 0

        curSum = 0
        prefSum = {0: -1}
        minLen = len(nums)

        for i, num in enumerate(nums):
            curSum = (curSum + num) % p
            prefix = (curSum - rem + p) % p

            if prefix in prefSum:
                minLen = min(minLen, i - prefSum[prefix])

            prefSum[curSum] = i

        if minLen == len(nums):
            return -1
        return minLen

