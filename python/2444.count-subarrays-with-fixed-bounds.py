class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        """
        1,3,5,2,7,5

        1,3,5,2,1,7,5

        1,1,1,1,0,1,1,1
        """

        total = 0
        n = len(nums)
        left = right = -1
        cut = -1

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                left = right = -1
                cut = i
            if nums[i] == minK:
                left = i
            if nums[i] == maxK:
                right = i

            if left != -1 and right != -1:
                total += min(left, right) - cut

        return total

