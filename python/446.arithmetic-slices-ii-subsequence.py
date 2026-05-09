class Solution:

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """Find number of arithmetic subsequences.

         j     i
        [2,    4,     6,         8,               10]
        dp
        [(), (2: 1), (4:1, 2:2), (6:1, 4:2, 2:3), (8:1, 6:2, 4:3, 2:4)]

        Time: O(n^2)
        Space: O(n^2)

        Args:
            nums: list of input numbers

        Returns:
            Number of arithmetic subsequences.

        """
        n = len(nums)
        res = 0
        # dp[i][diff] - number of sequences ending at i with difference diff
        dp = [{} for _ in range(n)]

        # for every index
        for i in range(n):
            # go for all the previous indexes
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
                res += dp[j].get(diff, 0)

        return res