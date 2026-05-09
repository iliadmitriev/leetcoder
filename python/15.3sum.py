class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, target in enumerate(nums):
            # optimization if current number is equal to previous
            # we don't want to use it twice
            if i > 0 and nums[i - 1] == target:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[left] + nums[right] + target
                if cur > 0:
                    right -= 1
                elif cur < 0:
                    left += 1
                else:
                    res.append((target, nums[left], nums[right]))
                    # shift only left pointer (right pointer will be shifted on the next iteration)
                    left += 1
                    # if pointer points to the same number 
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
        return res