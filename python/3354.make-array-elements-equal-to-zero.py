class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        selections = 0

        right = sum(nums)
        left = 0

        for num in nums:
            left += num
            right -= num

            if num != 0:
                continue

            if left == right:
                selections += 2
            elif abs(left - right) == 1:
                selections += 1

        return selections

