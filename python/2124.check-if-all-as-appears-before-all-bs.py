class Solution:
    def checkString(self, s: str) -> bool:
        start = False
        for ch in s:
            if ch == 'b':
                start = True
            if start and ch == 'a':
                return False
            
        return True