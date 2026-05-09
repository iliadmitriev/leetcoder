class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        Time: O(m^2 * n * log(m))
        Space: O(m * n)
        """
        m, n = len(matrix), len(matrix[0])
        
        def max_sub_arr_not_greater_k(arr: List[int], k: int) -> int:
            """
            Time: O(n * log(n))
            Space: O(n)
            n = lenght of arry
            """
            prefix_sum = [float('inf')]
            curr_sum = 0
            curr_max = float('-inf')
            for num in arr:
                bisect.insort(prefix_sum, curr_sum)
                curr_sum += num
                i = bisect.bisect_left(prefix_sum, curr_sum - k)
                curr_max = max(curr_max, curr_sum - prefix_sum[i])
            return curr_max
        
        # calculate prefix sum
        for y in range(m):
            for x in range(n - 1):
                matrix[y][x + 1] += matrix[y][x]
                
        res = float('-inf')
        for x1 in range(n):
            for x2 in range(x1, n):
                arr = [matrix[y][x2] - (matrix[y][x1 - 1] if x1 > 0 else 0) for y in range(m)]
                res = max(res, max_sub_arr_not_greater_k(arr, k))
                
        return res