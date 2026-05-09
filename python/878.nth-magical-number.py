class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        modulo = 10**9 + 7
        
        # from fractions import gcd
        L = (a * b) // gcd(a, b)
        M = L // a + L // b - 1
        q, r = divmod(n, M)
        # print(f'{n=}, {a=}, {b=}, {L=}, {M=}, {q=}, {r=}')
        
        lo = q * L
        hi = n * min(a, b)
        
        while lo < hi:
            mi = (lo + hi) // 2
            if mi // a + mi // b - mi // L < n:
                lo = mi + 1
            else:
                hi = mi
                
        return lo % modulo
                