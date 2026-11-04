class BalancedWindow:
    def __init__(self, length: int) -> None:
        self.bal = (length + 1) // 2  # balanced lower length
        self.lower = SortedList()  # lower + median
        self.upper = SortedList()  # upper
        self.upper_sum = 0
        self.lower_sum = 0

    def add(self, val: int) -> None:
        if not self.lower or val <= self.lower[-1]:
            self.lower.add(val)
            self.lower_sum += val
        else:
            self.upper.add(val)
            self.upper_sum += val

        self._rebalance()

    def remove(self, val: int) -> None:
        if val in self.lower:
            self.lower.remove(val)
            self.lower_sum -= val
        else:
            self.upper.remove(val)
            self.upper_sum -= val

        self._rebalance()

    def _rebalance(self) -> None:
        """Keep `lower` array size less or equal to target.
        The median value must be at the end of the `lower`.
        """
        while len(self.lower) > self.bal:
            val = self.lower[-1]
            self.lower.remove(val)
            self.lower_sum -= val
            self.upper.add(val)
            self.upper_sum += val

        while len(self.lower) < self.bal and self.upper:
            val = self.upper[0]
            self.upper.remove(val)
            self.upper_sum -= val
            self.lower.add(val)
            self.lower_sum += val

    def get_ops(self) -> int:
        med = self.lower[-1]
        lower = len(self.lower) * med - self.lower_sum  # count increase lower
        upper = self.upper_sum - len(self.upper) * med  # count decrease upper
        return lower + upper


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        """
        nums: given array
        x: subarray length
        k: number of subarrays

        [5,-2,1,3,7,3,6,4,-1], x = 3

        [5,-2,1] 7 : 4/3 => 1 4+3 = 7
        [-2,1,3] 5 v: 2/3 => 1 3+0+2 = 5
        [1,3,7] 6

        [3,7,3] 4
        [7,3,6] 4
        [3,6,4] 3 v
        [6,4,-1] 7

        """
        n = len(nums)
        win = BalancedWindow(x)
        ops = []

        for r in range(n):
            win.add(nums[r])

            l = r - x + 1
            if l < 0:
                continue

            ops.append(win.get_ops())
            win.remove(nums[l])

        INF = float("inf")
        # dp[current index][count of subarrays]
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for count in range(k + 1):
                # option 1: leave
                dp[i][count] = dp[i - 1][count]

                # option 2: take
                # only if needed (count > 0)
                # and there is x numbers left
                if count > 0 and i >= x:
                    start = i - x
                    candidate = dp[start][count - 1] + ops[start]
                    dp[i][count] = min(dp[i][count], candidate)

        return dp[n][k]
