class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        """
        
        [1,1,2,2,3,4,4,4]

        [1:1, 2:2, 3:1, 4:3]
        3 + 4 
        
        """
        n = len(nums)
        nums.sort()
        ops = 0
        for i in range(n - 1, 0, -1):
            if nums[i] != nums[i - 1]:
                ops += n - i

        return ops