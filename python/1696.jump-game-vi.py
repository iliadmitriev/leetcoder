class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """A Jump game simulation.
        
        A Dynamic programming approach using double ended queue
        to maintain sorted list of dp[j] values.

        Time: O(n)
        Space: O(n)

        Args:
            nums (list of int): numbers list
            k: maximum jump length

        Returns:
            (int): maximum cost you can achieve.
        """
        # double ended queue with tuples (index, dp value)
        # for saving k values (largest is leftmost)
        dq = deque()
        # dp[i] = nums[i] + max{ dp[j] }, where j: max(0, i - k) <= j <= (i - 1)
        curr = nums[0]
        for i in range(len(nums)):
            curr = nums[i] + (dq[0][1] if dq else 0)
            # find the place to put value
            # starting from the right and throwing
            # away values which is less than current value
            while dq and dq[-1][1] < curr:
                dq.pop()
            # add value to the right end
            dq.append((i, curr))

            # check left value index is between max(0, i - k) and (i - 1)
            # if left value index is reached i (less than or equal)
            if dq[0][0] <= i - k:
                dq.popleft()

        return curr
