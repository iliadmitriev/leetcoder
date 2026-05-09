class Solution:
    def minMaxDifference(self, num: int) -> int:
        val = []

        while num:
            val.append(num % 10)
            num //= 10

        maxReplace = next(iter(v for v in val[::-1] if v < 9), 9)
        minReplace = val[-1]
        minVal = 0
        maxVal = 0

        while val:
            v = val.pop()

            if v == maxReplace:
                vMax = 9
            else:
                vMax = v

            if v == minReplace:
                vMin = 0
            else:
                vMin = v

            minVal = minVal * 10 + vMin
            maxVal = maxVal * 10 + vMax

        return maxVal - minVal

