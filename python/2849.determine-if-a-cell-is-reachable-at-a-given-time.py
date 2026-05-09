class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if fx == sx and fy == sy:
            return t != 1
            
        dx = abs(fx - sx)
        dy = abs(fy - sy)

        return t >= max(dy, dx)