class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        """Calculate maximum length of subarray with positive product
                
        f - accumulate max positive count
        g - accumulate max negative count


        i:      0   1   2   3   4   5   6
        nums:   1  -2  -3   4   3  -1   2
        f:      1   0   3   4   5   0   0
        g:      0   2   1   2   3   0   0
        
        nums:   1   2   3   5  -6   4   0  10
        f:      1   2   3   4   
        g:      0   0   0   0   5


        :param nums: given list of numbers
        :return: length of subarray with positive product
        """
        
        f, g = 0, 0
        
        f_prev = 0
        g_prev = 0
            
        res = 0
            
            
        for i in range(len(nums)):
            if nums[i] > 0:
                # positive * previous positive => positive
                f = f_prev + 1
                
                # if previous was negative
                if g_prev:
                    # positive * negative => negative
                    g = g_prev + 1
                else:
                    g = 0
                
                
            if nums[i] < 0:
                # negative * previous positive => negative
                g = f_prev + 1
                
                if g_prev:
                    # negative * previous negative => positive
                    f = g_prev + 1
                else:
                    f = 0
                    
            if nums[i] == 0:
                f, g = 0, 0

            f_prev = f
            g_prev = g                
                    
            res = max(res, f)
        
        return res