class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        # dp[i] - length of longest increasing sequence for length i
        dp = []
        res = []
        for i, num in enumerate(obstacles):
            if not dp or dp[-1] <= num:
                dp.append(num)
                res.append(len(dp))
            else:
                index = bisect.bisect_right(dp, num)
                dp[index] = num
                res.append(index + 1)  # +1 for converting index to length starting from 0
        
        return res