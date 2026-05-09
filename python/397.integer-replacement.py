class Solution:
    def integerReplacement(self, n: int) -> int:
        i = 0
        while n != 1:

            if 1 & n:
                # check if 2nd LSB is equal to `1`
                # and check if there is bits after 2nd LSB, 
                # excluding special case n == 3
                if (n >> 1) & 1 and n >> 2:
                    n += 1
                else:
                    n -= 1
                    
            else:
                # divide by 2
                n >>= 1
            i += 1
            
        return i