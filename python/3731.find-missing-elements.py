class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        prev = nums[0]
        i = 1

        while i < len(nums):
            if prev + 1 != nums[i]:
                res.append(prev + 1)
                prev += 1
            else:
                prev = nums[i]
                i += 1

        return res
