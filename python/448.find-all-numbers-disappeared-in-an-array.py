class Solution:
    def findDisappearedNumbers(self, nums):
        return list(set(i + 1 for i in range(len(nums))) - set(nums))
