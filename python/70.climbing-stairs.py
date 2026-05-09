class Solution:
    def climbStairs(self, n: int) -> int:
        # need to remember 2 previous steps
        prev, cur = 0, 1
        
        for i in range(n):
            prev, cur = cur, prev + cur
            
        return cur
    