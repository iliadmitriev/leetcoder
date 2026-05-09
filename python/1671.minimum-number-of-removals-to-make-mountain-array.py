class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        n = len(nums)

        lis = [1] * n  # longesg increasing subsequence
        lds = [1] * n  # longest decreasing subsequence

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        for j in range(n - 1, -1, -1):
            for i in range(j, n):
                if nums[j] > nums[i]:
                    lds[j] = max(lds[j], lds[i] + 1)

        minRemoval = n
        for i in range(1, n - 1):
            if min(lis[i], lds[i]) < 2:
                continue

            minRemoval = min(minRemoval, n - lis[i] - lds[i] + 1)

        return minRemoval

