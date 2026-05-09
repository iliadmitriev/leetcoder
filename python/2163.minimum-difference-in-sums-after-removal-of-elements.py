import heapq


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        m = len(nums)
        n = m // 3

        # left max heap queue to maintain n elements to get rid of
        left = [-nums[i] for i in range(n)]
        prefix = [-sum(left)]

        heapq.heapify(left)  # nlogn

        for i in range(n, 2 * n):  # n
            p = prefix[-1]
            cur = nums[i]

            prev = -heapq.heappushpop(left, -cur)  # logn
            p += cur - prev

            prefix.append(p)

        right = [nums[i] for i in range(2 * n, m)]
        suffix = [sum(right)]

        heapq.heapify(right)  # nlogn

        for i in range(2 * n - 1, n - 1, -1):  # n
            p = suffix[-1]
            cur = nums[i]

            prev = heapq.heappushpop(right, cur)  # logn
            p += cur - prev

            suffix.append(p)

        suffix.reverse()

        min_diff = prefix[0] - suffix[0]

        for i in range(n + 1):  # n
            min_diff = min(min_diff, prefix[i] - suffix[i])

        return min_diff

