class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """Count vovels permutations.
        
        Time: O(n)
        """
        modulo = int(1e9 + 7)
        
        a, e, i, o, u = 1, 1, 1, 1, 1
        
        # count of vowel is equal to sum of counts after wich it can follow 
        # a =  e + i + u
        # e = a + i
        # i = e + o
        # o = i
        # u = i + o
        for _ in range(1, n):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        
        return (a + e + i + o + u) % modulo