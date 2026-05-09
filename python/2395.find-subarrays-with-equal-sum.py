class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        seen = set()

        for i in range(len(nums) - 1):
            sub = nums[i] + nums[i + 1]

            if sub in seen:
                return True

            seen.add(sub)

        return False

