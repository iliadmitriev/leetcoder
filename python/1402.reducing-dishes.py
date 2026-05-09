class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res, curr = 0, 0
        for num in sorted(satisfaction, reverse=True):
            curr += num
            if curr < 0:
                break

            res += curr

        return res