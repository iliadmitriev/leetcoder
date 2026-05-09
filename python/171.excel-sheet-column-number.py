class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i, c in enumerate(columnTitle[::-1]):
            total += (ord(c) - 64) * (26**i)
        
        return total