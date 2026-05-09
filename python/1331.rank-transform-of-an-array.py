class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        rank = {}
        curRank = 1

        for num in sorted(arr):
            if num not in rank:
                rank[num] = curRank
                curRank += 1

        return [rank[num] for num in arr]

