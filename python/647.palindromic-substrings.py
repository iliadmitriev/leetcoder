class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Time: O(n ^ 2)
        Space: O(n ^ 2)
        """
        
        n = len(s)
        # if (i, j) in dp this means there is palindorme from i to j
        dp = set()
        
        count = 0
        
        # l - length of possible palindrome
        # starts from 1 to n
        for l in range(0, n):
            for i in range(0, n - l):
                if s[i] == s[i + l] and (l == 0 or (i + 1, i + l - 1) in dp or i == i + l - 1):
                    dp.add((i, i + l))
                    count += 1
                    
        return count
            