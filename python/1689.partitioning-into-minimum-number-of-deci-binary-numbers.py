class Solution:
    def minPartitions(self, n: str) -> int:
        for i in reversed(range(10)):
            if str(i) in n:
                return i
        return 0