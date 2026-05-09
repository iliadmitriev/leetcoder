class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        first_second, first = 0, 0
        for num in nums:
            first_second = first_second ^ num

        mask = first_second & ~(first_second - 1)

        for num in nums:
            if num & mask:
                first = first ^ num

        return [first, first_second ^ first]

