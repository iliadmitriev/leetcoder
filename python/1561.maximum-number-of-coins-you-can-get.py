class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        my = len(piles) - 2
        my_score = 0
        
        for _ in range(len(piles) // 3):
            my_score += piles[my]
            my -= 2

        return my_score