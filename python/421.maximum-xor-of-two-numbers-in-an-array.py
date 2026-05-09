class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        """
        Idea:
        Let's suppose we have m = n_i ^ n_j maximum number what we are looking for.
        Since XOR is both commutative and assosiative, we can say:
        m ^ n_j = n_i
        
        so we have to guess bits of `m` with each `n_j`
        checking if combination of `m` and `n_j` will produce `n_i`
        
        
        Algorithm:
        1) Start iteration from MSB to LSB (31 to 0):
            a) create bitmask as number of iterated bits
            b) build set of prefixes to all numbers using bitmask
            c) iterate prefixes and check:
                if result bits (with appended current bit) XOR'ed with one of prefixes is producing any other prefix:
                then, we append current bit it to result bits
                
        Time: O(m * n)
        n - lenght of numbers list
        m - number of bits (32)
        """
        res = 0
        bitmask = 0
        
        for i in range(31, -1, -1):
            bitmask |= 1 << i
            
            prefixes = { num & bitmask for num in nums }
            
            tmp = res | (1 << i)
            
            if any(tmp ^ prefix in prefixes for prefix in prefixes):
                res = tmp
                
        return res