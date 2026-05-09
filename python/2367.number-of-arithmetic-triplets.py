class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0

        double: set[int] = set()
        triple: set[int] = set()

        for num in nums:
            if num in triple:
                count += 1

            if num in double:
                triple.add(num + diff)

            double.add(num + diff)

        return count

