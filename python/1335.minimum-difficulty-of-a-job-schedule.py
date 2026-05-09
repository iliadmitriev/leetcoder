class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        Time: O(n**2 * d)
        n - number of jobs
        d - number of days
        Space: O(n * d)
        """
        # number of jobs
        n = len(jobDifficulty)
        @cache
        def dp(j: int, d: int) -> int:
            """Count sum daily job maximus difficulty splitting jobs to days.
            
            Args:
                j (int): starting position
                d (int): number of days to split jobs
            """
            # spent one day
            d -= 1
            # ending condition:
            # if all days are spend return maximum of jobs thats left undone
            if d == 0:
                return max(jobDifficulty[j:])
            # init result
            res = float('inf')
            
            # calculate max of different splits
            # but leaving some jobs for the last days
            for i in range(j + 1, n - d + 1):
                res = min(res, max(jobDifficulty[j:i]) + dp(i, d))
            
            return res
            
        # return result if jobs can be splited among all the days
        # otherwise return -1
        return dp(0, d) if d <= n else -1