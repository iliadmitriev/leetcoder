class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        suffix: list[int] = [0] * 51
        prefix: list[int] = [0] * 51

        suffixCount = 0
        prefixCount = 0

        for num in nums:
            suffix[num] += 1
            if suffix[num] == 1:
                suffixCount += 1

        res: list[int] = []

        for num in nums:
            prefix[num] += 1
            suffix[num] -= 1

            if suffix[num] == 0:
                suffixCount -= 1
            if prefix[num] == 1:
                prefixCount += 1

            res.append(prefixCount - suffixCount)

        return res

