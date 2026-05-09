class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        for num in arr:
            if num - prev > 1:
                num = prev + 1
            prev = num

        return prev