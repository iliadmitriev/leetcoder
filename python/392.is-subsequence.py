class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        s - input string
        t - template
        
        Time: O(n)
        Space: O(1)
        """
        i = 0
        for ch in s:
            k = i
            while k < len(t) and t[k] != ch:
                k += 1
            if k == len(t):
                return False
            i = k + 1

        return True

