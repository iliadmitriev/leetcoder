from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {k: v for v, k in enumerate(arr2)}
        arr1.sort(key=lambda x: order.get(x, x + len(arr2)))
        return arr1

