class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s))) # O(n**2)
        return ''.join(sorted(s)) # O(n * log(n))