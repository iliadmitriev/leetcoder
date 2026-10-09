class Solution:
    def minInsertions(self, s: str) -> int:
        closing_needed = 0
        res = 0
        
        for ch in s:
            if ch == "(":
                closing_needed += 2
                
                if closing_needed % 2 == 1:
                    res += 1
                    closing_needed -= 1
                    
            elif ch == ")":
                closing_needed -= 1
                
                if closing_needed < 0:
                    res += 1
                    closing_needed += 2
                    
        return res + closing_needed