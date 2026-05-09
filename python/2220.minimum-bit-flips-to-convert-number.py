class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return int(start ^ goal).bit_count()

