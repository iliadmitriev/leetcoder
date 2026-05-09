from collections import Counter


class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        cnt = Counter(nums)

        for count in cnt.values():
            if count % 2:
                return False

        return True

