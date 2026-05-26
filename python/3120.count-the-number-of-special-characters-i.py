class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)
        res = 0
        
        for ch in string.ascii_lowercase:
            if ch in s and ch.upper() in s:
                res += 1

        return res