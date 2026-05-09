class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        res = []
        
        for num in nums:  # iterate: O(n)
            # find index (leftmost) in sorter array 
            # this index will be count of elements smaller than num 
            idx = bisect_left(temp, num) # binary search O(logn)
            res.append(idx)
            del temp[idx]
        
        return res
        