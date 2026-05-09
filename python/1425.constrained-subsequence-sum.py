import heapq


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        k = 2
        16, -13, -5, -10,  4,  3,  9
        0   16   16   11   11  15  18  - max of window size k
        16  3    11   1    15  18  27  - max + i-th

        k = 2
        10,  2, -10,  5,  20
        0   10   12  12   17
        10  12    2  17   37

        k = 1
        -1,  -2,  -3
         0   -1   -3
        -1   -3   -6

        k = 2
        10, -2, -10, -5, 20
        0   10   10   8   3
        10   8    0   3  23 
        """
        n = len(nums)
        q = deque()
        dp = [0] * n

        for i in range(n):
            
            # drop all indexes that greater than window size from the left 
            while q and i - q[0] > k:
                q.popleft()

            # calculate dp[i]
            dp[i] = (dp[q[0]] if q else 0) + nums[i]

            # drop all indexes that value is less or equal from the right
            while q and dp[q[-1]] <= dp[i]:
                q.pop()
            
            if dp[i] > 0:
                q.append(i)

        return max(dp)


