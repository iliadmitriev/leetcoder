from functools import reduce
import operator

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # filter all the strings from array that has not uniq characters
        uniq = list(filter(lambda c: len(c) == len(set(c)), arr))
        # lambda function to build mask from string acd -> 0b1101
        mask = lambda s: reduce(operator.or_, map(lambda c: 1 << (ord(c) - 97), s), 0)
        # convert strings to masks, and get their lengths
        masked = list(map(mask, uniq))
        lenghts = list(map(len, uniq))
        
        @cache
        def dp(curr_mask: int, curr_len: int) -> int:
            """
            Args:
                curr_mask (int): current mask of used chars
                curr_len (int): current lenght of chars
            
            Returns:
                (int): maximum length
            """
            res = curr_len
            for i, m in enumerate(masked):
                if m & curr_mask == 0:
                    new_len = dp(m | curr_mask, curr_len + lenghts[i])
                    res = max(res, new_len)
                    
            return res
        
        return dp(0, 0)