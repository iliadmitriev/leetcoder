import collections


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        count = collections.Counter(moves)

        return abs(count["L"] - count["R"]) + count["_"]
