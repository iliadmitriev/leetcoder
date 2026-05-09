class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        
        for i, num in enumerate(sorted(nums)):
            if num not in count:
                count[num] = i
                
        return [count[n] for n in nums]
    