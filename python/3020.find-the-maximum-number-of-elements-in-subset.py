import math


class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        ones = cnt.pop(1, 1)
        res = max(0, ones - 1 + (ones & 1))

        pre = defaultdict(int)

        for num in sorted(cnt.keys()):
            r = int(math.sqrt(num))

            if r * r == num and cnt[r] >= 2 and pre[r] > 0:
                pre[num] = pre[r] + 2
            else:
                pre[num] = 1

            res = max(res, pre[num])


        return res