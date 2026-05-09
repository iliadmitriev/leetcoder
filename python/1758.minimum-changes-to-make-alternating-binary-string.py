class Solution:
    def minOperations(self, s: str) -> int:
        one = sum(int(ch) == i % 2 for i, ch in enumerate(s))

        return min(one, len(s) - one)