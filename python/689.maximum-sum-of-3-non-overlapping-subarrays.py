from functools import cache


class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:

        prefix = []
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if i >= k:
                curSum -= nums[i - k]
            if i >= k - 1:
                prefix.append(curSum)

        @cache
        def dfsGetMaxSum(i: int, cnt: int) -> int:
            if cnt == 3 or i > len(nums) - k:
                return 0

            # inlucde
            include = prefix[i] + dfsGetMaxSum(i + k, cnt + 1)

            # skip
            skip = dfsGetMaxSum(i + 1, cnt)

            return max(include, skip)

        def getIndeces() -> list[int]:
            i = 0
            indices = []

            while i <= len(nums) - k and len(indices) < 3:
                include = prefix[i] + dfsGetMaxSum(i + k, len(indices) + 1)
                skip = dfsGetMaxSum(i + 1, len(indices))

                if include >= skip:
                    indices.append(i)
                    i += k

                else:
                    i += 1

            return indices

        return getIndeces()

