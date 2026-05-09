class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType) // 2
        unique = len(set(candyType))

        return min(unique, n)

