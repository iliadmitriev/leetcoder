import collections
import bisect


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        res = [-1] * m
        indices = collections.defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)

        for ind in indices.values():
            x = ind[0]  # remember first element
            ind.insert(0, ind[-1] - n)  # put circular of last element to begining
            ind.append(x + n)  # put circular of first element to end

        for j, q in enumerate(queries):
            x = nums[q]

            # if x is not in the nums of number of such element less than 2 (2 extra elements)
            if x not in indices or len(indices[x]) < 4:
                continue  # skip

            ind = indices[x]

            i = bisect.bisect_left(ind, q)
            res[j] = min(
                ind[i + 1] - ind[i],
                ind[i] - ind[i - 1],
            )

        return res
