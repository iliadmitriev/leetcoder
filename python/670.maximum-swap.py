class Solution:
    def maximumSwap(self, num: int) -> int:
        val: list[int] = []
        while num:
            val.append(num % 10)
            num //= 10

        mm = []
        curMax, idx = -1, -1

        for i, v in enumerate(val):
            if v > curMax:
                curMax = v
                idx = i

            mm.append((curMax, idx))

        for i in range(len(val) - 1, -1, -1):
            if val[i] < mm[i][0]:
                val[i], val[mm[i][1]] = val[mm[i][1]], val[i]
                break

        num = 0
        while val:
            num *= 10
            num += val.pop()

        return num

