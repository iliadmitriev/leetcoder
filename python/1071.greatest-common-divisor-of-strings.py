class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def check(k: int) -> bool:
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == base * n1 and str2 == base * n2

        
        for k in range(min(len1, len2), 0, -1):
            if check(k):
                return str1[:k]
        return ""