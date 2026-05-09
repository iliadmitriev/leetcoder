class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        n = len(nums)

        leftPref = [nums[0]]
        rightPref = [nums[-1]]

        for i in range(1, n):
            leftPref.append(min(leftPref[-1], nums[i]))
            rightPref.append(min(rightPref[-1], nums[n - i - 1]))

        return min(
            (
                nums[i] + leftPref[i] + rightPref[n - i - 1]
                for i in range(1, n - 1)
                if nums[i] > leftPref[i] and nums[i] > rightPref[n - i - 1]
            ),
            default=-1,
        )

