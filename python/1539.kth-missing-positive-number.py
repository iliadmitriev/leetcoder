class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k

        left, right = 0, len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= mid + k:
                left = mid + 1
            else:
                right = mid
        
        return left + k