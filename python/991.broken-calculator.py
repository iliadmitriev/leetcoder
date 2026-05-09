class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        while target > startValue:
            if target % 2:
                target += 1
            else:
                target //= 2
            ops += 1
            
            
        return ops + (startValue - target)