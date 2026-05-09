class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """Max points from cards.
        
        Finds max points you can obtain from taking cards.
        
        Time: O(n)
        Space: O(1)
        
        Idea:
        Main idea is to use sliding window to 
        calculate minimum points in a subsequence
        length of (n - k) and then subtract from total sum
        """
        n, total = len(cardPoints), sum(cardPoints)
        
        remaining_points = n - k
        window = sum(cardPoints[:remaining_points])
        min_sum = window
        for i in range(remaining_points, n):
            window = window + cardPoints[i] - cardPoints[i - remaining_points]
            min_sum = min(min_sum, window)
            
        return total - min_sum
        
        