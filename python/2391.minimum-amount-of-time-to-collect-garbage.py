class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = sum(map(len, garbage))
        travel.append(0)
        m, g, p = 0, 0, 0
        f = 0

        for i, house in enumerate(garbage):
            f += travel[i - 1]
            house = set(house)

            if 'M' in house:
                m = f
            if 'P' in house:
                p = f
            if 'G' in house:
                g = f

        return total + m + g + p