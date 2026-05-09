from collections import Counter


class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res1, res2 = 0, 0
        h1 = Counter(nums1)
        h2 = Counter(nums2)

        for num in nums1:
            res1 += h2[num] > 0

        for num in nums2:
            res2 += h1[num] > 0

        return [res1, res2]

