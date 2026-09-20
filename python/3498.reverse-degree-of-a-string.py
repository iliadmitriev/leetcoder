class Solution:
    def reverseDegree(self, s: str) -> int:
        base = ord('a') + 26
        return sum(map(lambda v: v[0] * (base - ord(v[1])), enumerate(s, start=1)))