class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
               i
            j
        [1, 3, 5, 4, 7]

        [1, 2, 3, 3, 4]
        [1, 1, 1, 1, 1]
         
        """
        n = len(nums)
        # lenght[i] - length of LIS ending at i
        length = [1] * n
        # count[i] - count of LIS ending at i
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        count[i] = 0
                        length[i] = length[j] + 1
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_len = max(length)
        return sum(cnt for i, cnt in enumerate(count) if length[i] == max_len)