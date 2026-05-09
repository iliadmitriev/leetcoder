class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        Binary search aproach
        
        Idea:
        1. lower bound is maximal number in the array (case when m == len(nums))
        2. upper bound is sum of all numbers in the array (case when m == 1)
        3. use binary search to find minimal of the largest sum amount subarrays.
           оn each iteration:
           - find the middle between lower and upper bound
           - calculate count of splits which is lower than or equal to the middle
           - if count of splits is bigger than m,
             then move lower bound to the next element from the middle
             (to decrease count of splits)
             otherwise move upper bound to the middle
             (to make count of splits bigger)
           
        """
        
        lower, upper = max(nums), sum(nums)
        
        while lower < upper:
            
            middle = (lower + upper) // 2
            
            # calculate count of splits
            cnt, total = 1, 0
            for num in nums:
                if total + num <= middle:
                    total += num
                else:
                    total = num
                    cnt += 1
                    
            if cnt > m:
                lower = middle + 1
            else:
                upper = middle
                
        return upper