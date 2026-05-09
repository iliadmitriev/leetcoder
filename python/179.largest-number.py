class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        numsStr = list(map(str, nums))

        numsStr.sort(key=lambda x: x * 10, reverse=True)

        if numsStr[0] == "0":
            return "0"

        return "".join(numsStr)

