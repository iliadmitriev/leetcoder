import collections
import bisect

"""
[2,2,2,2,2]
[0,1,2,3,4]

0 2  =>  0 0 5 10
1 2  =>  1 1 4 9
2 2  =>  2 3 3 7
3 2  =>  3 6 2 4
4 2  =>  4 10 1 0

0: 0-0 + 1-0 + 2-0 + 3-0 + 4-0 => 10
1: 0-1 + 1-1 + 2-1 + 3-1 + 4-1 => 7
2: 0-2 + 1-2 + 2-2 + 3-2 + 4-2 => 6
3: 0-3 + 1-3 + 2-3 + 3-3 + 4-3 => 7
4: 0-4 + 1-4 + 2-4 + 3-4 + 4-4 => 10

"-" sign is a modular difference x-y = x - y if x > y else y - x
"""


class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        c = collections.defaultdict(list)  # indices gouped by x
        s = collections.defaultdict(int)  # total sum of all numbers x

        for i, x in enumerate(nums):
            c[x].append(i)
            s[x] += i

        res = [0] * n

        for x, indices in c.items():
            m = len(indices)
            left_sum = 0  # left sum of indices (except current)
            right_sum = 0  # right sum of indices (except current)
            total = s[x]  # total sum of indices

            for i in range(m):
                # recalculate right sum of indices
                right_sum = total - left_sum - indices[i]

                # left and right contributions
                # left sum is subtracted (-), right sum is added (+)
                # indices[i] is value of index
                # i is number of left indices, added
                # m - i - 1 is a number of right indices, subtracted
                left = indices[i] * i - left_sum
                right = right_sum - indices[i] * (m - i - 1)

                res[indices[i]] = left + right

                left_sum += indices[i]

        return res
