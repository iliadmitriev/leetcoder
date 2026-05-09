class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # take inf as an answer
        closest_result = inf
        for i in range(len(nums) - 2):
            # optimization 1 (if answer is the first 3 numbers)
            largest = nums[i] + nums[-1] + nums[-2]
            if largest < target:
                if abs(target - largest) < abs(target - closest_result):
                    closest_result = largest
                continue

            # optimiztation 2 (if answer is the last 3 numbers)
            smallest =  nums[i] + nums[i + 1] + nums[i + 2]
            if smallest > target:
                if abs(target - smallest) < abs(target - closest_result):
                    closest_result = smallest
                break

            
            left, right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == target:
                    return cur
                elif cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
                if abs(cur - target) < abs(closest_result - target):
                    closest_result = cur
        return closest_result