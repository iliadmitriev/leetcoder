import functools as ft
import operator as op


class Solution:
    def xorAllNums(self, nums1: list[int], nums2: list[int]) -> int:
        odd1, odd2 = len(nums1) % 2, len(nums2) % 2
        ans = 0

        if odd2:
            ans = ft.reduce(op.xor, nums1, ans)

        if odd1:
            ans = ft.reduce(op.xor, nums2, ans)

        return ans

