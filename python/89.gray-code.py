class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        1. set base array for n = 1 [0, 1]
        2. while base < target number of combinations
            a) extend result array with its mirror copy, adding base to it
            b) shift base by 1 for next step
        """
        res = [0, 1]
        base = 2
        while base < 2 ** n:
            res.extend([r ^ base for r in res[::-1]])           
            base <<= 1

        return res