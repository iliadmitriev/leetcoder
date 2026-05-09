class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(
            n - min(right, default=n),
            max(left, default=0)
        )