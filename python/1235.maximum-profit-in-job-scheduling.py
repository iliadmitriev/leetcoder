from bisect import bisect_left
from operator import itemgetter


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """Find max profit from jobs without overlapping.

        Args:
            startTime (List of int): list of timestamps when job starts.
            endTime (List of int): list of timestamps when job finishes.
            profit (List of int): list of jobs profits.

        Time: O(n * log(n))
        Space: O(n)

        Returns:
            (int): max profit from jobs without overlapping.

        """
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        ending = itemgetter(0) # end time getter
        pr = itemgetter(1) # profit getter

        # tuples of (endtime, current max profit)
        dp = [(0, 0)]

        for start, end, prof in jobs:
            i = bisect.bisect_left(dp, start + 1, key=ending) - 1
            
            cur_profit = prof + pr(dp[i])
            if cur_profit > pr(dp[-1]):
                dp.append((end, cur_profit))

        return pr(dp[-1])