class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        """
        Time: O(m * k * log(v * m))
        v - maximum value, v <= 5000
        m - number of rows, m <= 40
        k - target, k <= min(200, n ^ m)
        """
        # return sum(sorted(list(product(*mat)), key=sum)[k - 1])
        m, n = len(mat), len(mat[0])
        # if m == 1:
        #     return mat[0][k - 1]

        def count_number(target_sum, target_count, row=0, curr_sum=0):
            """Count number of arrays with sum less than target_sum.
            
            DFS for count of arrays with sum less than target_sum.
            break if target_count is reached (we only need to know the fact of overflow)

            Time: O(m * k)
            m - rows, n - columns, k - target element
            Best: m * min(k, n ^ 1)
            Worst: 1 * min(k, n ^ m)
            General: (m - i + 1) * min(k, n ^ i), 0 < i <= m
            
            """
            # overflow
            if curr_sum > target_sum:
                return 0
            # base case: we reached final row without overflow
            if row == m:
                return 1
            # iterate all the columns for row `row`
            # counting possible number of arrays to `res`
            res = 0
            for col in range(n):
                cnt = count_number(target_sum, target_count - res, row + 1, curr_sum + mat[row][col])
                # if count is 0, we don't need to 
                if cnt == 0:
                    break
                # add to possible count
                res += cnt
                # if result overflows k we don't need to count further
                if res > target_count:
                    break
            return res


        # O(log (5000 * m)), m <= 40
        left, right = m, 5000 * m
        while left < right:
            mid = (left + right) // 2
            if count_number(mid, k) < k:
                left = mid + 1
            else:
                right = mid

        return left
