class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        total = 0
        n = len(nums)
        i = 0
        curMax, curCnt = max(nums), 0

        for j in range(n):
            if curMax == nums[j]:
                curCnt += 1

            while curCnt >= k:
                if nums[i] == curMax:
                    curCnt -= 1

                i += 1

            total += i

        return total

