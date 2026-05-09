from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Use hashmap.

        Iterate first list and add to hashmap. Then iterate second list,
        if element is already in hashmap, add to result.
        """

        cache = {}
        for num in nums1:
            cache[num] = 1
        res = []
        for num in nums2:
            if num in cache and cache[num] == 1:
                res.append(num)
                cache[num] = 2

        return res

