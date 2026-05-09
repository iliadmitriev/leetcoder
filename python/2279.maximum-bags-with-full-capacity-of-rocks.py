from collections import Counter


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = Counter(map(lambda x: x[0] - x[1], zip(capacity, rocks)))
        res = 0
        for value, count in sorted(diff.items()):
            if value * count <= additionalRocks:
                res += count
                additionalRocks -= count * value
            else:
                leftover = int(additionalRocks / value)
                res += leftover
                additionalRocks -= leftover * value
                break
        return res