import statistics


class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        return statistics.multimode(nums)

        sneaky = []

        n = len(nums)
        cache = [False] * (n - 2)

        for v in nums:
            if cache[v]:
                sneaky.append(v)

            cache[v] = True

        return sneaky

