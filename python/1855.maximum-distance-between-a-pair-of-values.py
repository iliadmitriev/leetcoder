class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        max_dist = 0

        def bisect_right(arr: list[int], x: int, lo: int = 0, hi = None) -> int:
            if hi is None:
                hi = len(arr)
            res = 0

            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] >= x:
                    lo = mid + 1
                    res = mid
                else:
                    hi = mid

            return res            

        for i, num in enumerate(nums1):
            j = bisect_right(nums2, num, i)
            max_dist = max(max_dist, j - i)

        return max_dist
