class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        def zero_pos(arr: list[int], lo=0, hi=None) -> int:
            if not hi:
                hi = len(arr)

            if arr[0] < 0:
                return 0

            if arr[-1] > 0:
                return len(arr)

            # left, right = lo, hi
            # while left < right:
            #     mid = (left + right) // 2
            #     if arr[mid] >= 0:
            #         left = mid + 1
            #     else:
            #         right = mid
            # return left

            for i in range(hi, 0, -1):
                if arr[i - 1] >= 0:
                    return i

            return 0

        count = 0

        m, n = len(grid), len(grid[0])
        cur = n

        for r in range(m):
            cur = zero_pos(grid[r], 0, cur)

            count += n - cur

        return count

