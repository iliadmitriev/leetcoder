class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        flag = bool(n & 1)
        while n:
            n >>= 1
            if flag == bool(n & 1):
                return False
            flag = bool(n & 1)
        return True