class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.pop(-1)
        path = 0
        for i, num in enumerate(nums):
            if path < num + i:
                path = num + i
            if path <= i:
                return False
        return True