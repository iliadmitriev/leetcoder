class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        count = len(nums)
        total = sum(nums)
        acc = 0
        min_diff_avg_idx = 0
        min_diff_avg = inf
        for i in range(count):
            acc += nums[i]
            total -= nums[i]
            count -= 1

            diff_avg = abs(acc // (i + 1) - (total // count if count else 0))

            if diff_avg < min_diff_avg:
                min_diff_avg = diff_avg
                min_diff_avg_idx = i

        return min_diff_avg_idx