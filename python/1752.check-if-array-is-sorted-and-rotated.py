class Solution:
    def check(self, nums: list[int]) -> bool:
        rotations = 0
        prev = nums[0]

        # optimization: if the array is not rotated
        # then drop available rotation
        if nums[0] < nums[-1]:
            rotations += 1

        for i in range(len(nums)):
            if nums[i] < prev:
                rotations += 1

            if rotations > 1:
                return False

            prev = nums[i]

        return rotations <= 1

