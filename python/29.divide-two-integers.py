class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        sign = 1
        
        if dividend < 0:
            sign = -sign
            dividend = abs(dividend)
            
        if divisor < 0:
            sign = -sign
            divisor = abs(divisor)
                                
        if divisor == 0 and dividend > 0:
            return 2147483647
        elif divisor == 0 and dividend < 0:
            return -2147483648

        quotent = 0
        
        while dividend >= divisor:
            shift = 0
            
            while dividend > divisor << (shift + 1):
                shift += 1
            
            dividend -= divisor << shift
            quotent += 1 << shift
        
        return quotent * sign