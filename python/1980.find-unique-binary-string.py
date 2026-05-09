from functools import partial


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        binToInt = partial(int, base=2)
        exc = set(map(binToInt, nums))
        n = len(nums[0])

        for x in range(1 << n):
            if x not in exc:
                return bin(x)[2:].zfill(n)

        return ""

