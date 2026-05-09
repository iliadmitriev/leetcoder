class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def get_sum(value: int, index: int, n: int) -> int:
            # left sub array sum
            left_offset = max(value - index, 0)
            result = (value + left_offset) * (value - left_offset + 1) // 2
            # right sub array sum
            right_offset = max(value - ((n - 1) - index), 0)
            result += (value + right_offset) * (value - right_offset + 1) // 2
            return result - value

        maxSum -= n
        left, right = 0, maxSum + 1
        while left < right:
            mid = (left + right) // 2
            if get_sum(mid, index, n) <= maxSum:
                left = mid + 1
            else:
                right = mid
        
        return left