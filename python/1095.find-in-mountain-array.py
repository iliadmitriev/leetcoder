# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        @cache
        def _get(key: int) -> bool:
            return mountain_arr.get(key)

        def _bsearch(lo: int, hi: int, fn: Callable[[int], bool]) -> int:
            while lo < hi:
                mid = (lo + hi) // 2
                if fn(mid):
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        length = mountain_arr.length()
        peak = _bsearch(1, length - 2, lambda i: _get(i) < _get(i + 1))
        
        left = _bsearch(0, peak, lambda i: _get(i) < target)
        if _get(left) == target:
            return left

        right = _bsearch(peak + 1, length - 1, lambda i: _get(i) > target)
        if _get(right) == target:
            return right

        return -1