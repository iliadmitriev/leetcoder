class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left(arr: List[int], target: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo if lo < len(arr) and arr[lo] == target else -1
        
        def right(arr: List[int], target: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo - 1 if lo - 1 >= 0 and arr[lo - 1] == target else -1
       
        return [left(nums, target), right(nums, target)]