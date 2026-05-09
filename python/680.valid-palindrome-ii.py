class Solution:
    def validPalindrome(self, s: str) -> bool:

        def pal(i: int, j: int, r: bool = False) -> bool:
            while i < j:
                if s[i] != s[j]:
                    if r:
                        return False
                    return pal(i + 1, j, True) or pal(i, j - 1, True)
                i += 1
                j -= 1
            return True
        
        return pal(0, len(s) - 1)
        

        
        