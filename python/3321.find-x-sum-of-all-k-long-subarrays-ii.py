import collections as cc

import sortedcontainers as sc


class Solution:
    def findXSum(self, nums: list[int], k: int, x: int) -> list[int]:
        top: sc.SortedList[tuple[int, int]] = sc.SortedList()  # list[freq, num]
        remain: sc.SortedList[tuple[int, int]] = sc.SortedList()  # list[freq, num]
        freq: dict[int, int] = cc.defaultdict(int)  # num -> freq
        cur_sum = 0
        res: list[int] = []

        def balance():
            nonlocal cur_sum

            if len(top) < x and remain:
                f, n = remain.pop(0)
                top.add((f, n))
                cur_sum += f * n

            if top and remain and top[0] < remain[-1]:
                f1, n1 = top.pop(0)
                f2, n2 = remain.pop()
                top.add((f2, n2))
                remain.add((f1, n1))
                cur_sum += f2 * n2 - f1 * n1

        def update(num: int, delta: int = 1):
            nonlocal cur_sum
            if num in freq:
                prev = (freq[num], num)
                if prev in top:
                    top.remove(prev)
                    cur_sum -= prev[0] * prev[1]
                else:
                    remain.remove(prev)

            freq[num] += delta
            if freq[num] == 0:
                del freq[num]
            else:
                remain.add((freq[num], num))
            balance()

        for i in range(k):
            update(nums[i])

        res.append(cur_sum)

        for i in range(k, len(nums)):
            update(nums[i - k], -1)
            update(nums[i])
            res.append(cur_sum)

        return res

