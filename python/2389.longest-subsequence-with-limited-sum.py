from itertools import accumulate
from bisect import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
            1. Sort input data (order doesn't matter)
            2. Build accumulated list
               (need to find the longest sequence with a certain amount,
               so you need to take the minimum values ​​first, left values first)
            3. Find query in accumulated list
        """
        accumulated = list(accumulate(sorted(nums)))
        res = map(lambda q: bisect(accumulated, q), queries)
        return res

            