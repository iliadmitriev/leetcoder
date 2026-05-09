from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        """
        C^k_n - number of different ways to choose k elements randomly from n elements set.
        C^k_n = n! / (k! * (n - k)!)

        if k == 0 and n > 0 (how many ways to choose 0 elements from non empty set) => 1
        C^0_n = n! / n! * 0! = 1

        if k > 0 and n == 0 (how many ways to choose k elements from empty set) => 0

        C^k_0 = 0! / 0! * (-k)! - not defined (but equels to 0 in python)

        # number of ways to get k elements from n is equal to number of ways to get (n - k) elements from n
        C^k_n == C^(n - k)_n (C^left_total == C^right_total)

        Recurrent formula%:

        dfs(nums) = C^left_(total - 1) * dfs(left_nodes) * dfs(right_nodes)

        (total - 1) - exclude root element (it doesn't count)
        """
        mod = 10**9 + 7

        def dfs(nums: List[int]) -> int:
            n = len(nums)

            # don't count if it's less than 3
            if n < 3:
                return 1

            # first element is a root
            root = nums[0]

            left_nodes = [num for num in nums if num < root]
            right_nodes = [num for num in nums if num > root]

            return (dfs(left_nodes) * dfs(right_nodes) * comb(n - 1, len(left_nodes))) % mod

        # -1 is because we count additional ways (excluding given array order)
        return dfs(nums) - 1