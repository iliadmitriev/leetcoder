class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        
        1) invert rightmost non zero bit from the right number while it's bigger than left
        2) return right
        
        Time: O(log(n))
        Space: O(1)
        
        """

        while left < right:
            right &= right - 1
        
        return right