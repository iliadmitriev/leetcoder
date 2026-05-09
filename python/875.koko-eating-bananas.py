class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        if h == len(piles):
            return right

        while left < right:
            mid = (left + right) // 2

            hours = sum((pile - 1) // mid + 1 for pile in piles)

            if hours > h:
                left = mid + 1
            else:
                right = mid

        return left