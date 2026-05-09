class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def numMapper(num: int) -> int:
            if num == 0:
                return mapping[0]

            res = 0
            place = 1
            while num:
                res += place * mapping[num % 10]
                place *= 10
                num //= 10

            return res

        return sorted(nums, key=numMapper)

