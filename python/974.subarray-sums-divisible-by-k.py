from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        acc = 0
        cache = defaultdict(int)  # type: defaultdict[int, int]
        cache[0] = 1

        for num in nums:
            acc = (acc + num) % k
            res += cache[acc]
            cache[acc] += 1

        return res

