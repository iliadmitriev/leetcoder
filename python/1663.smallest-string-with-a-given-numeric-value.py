class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        z, carry = divmod(k - n - 1, 25)
        
        return 'a' * (n - z - 1) + chr(97 + carry + 1) + 'z' * z