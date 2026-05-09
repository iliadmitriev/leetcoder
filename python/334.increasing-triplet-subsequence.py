from itertools import accumulate

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """Two extra arrays.
        
        Time: O(n)
        Space: O(1)
        """
        first = inf
        second = inf
        for third in nums:
            if first >= third:
                first = third
            elif second >= third:
                second = third
            else:
                return True
            
        return False
