class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        total = sum(matchsticks)
        
        if total % 4:
            return False
        
        side = total // 4
        for match in matchsticks:
            if match > side:
                return False
        
        matchsticks.sort(reverse=True)
        
        @cache
        def dp(top: int, right: int, bottom: int, left: int, i: int) -> bool:
            if i == len(matchsticks):
                return top == right == bottom == left
            
            if top > side or right > side or bottom > side or left > side:
                return False
            
            return (
                dp(top + matchsticks[i], right, bottom, left, i + 1)
                or dp(top, right + matchsticks[i], bottom, left, i + 1)
                or dp(top, right, bottom + matchsticks[i], left, i + 1)
                or dp(top, right, bottom, left + matchsticks[i], i + 1)
            )
        
        return dp(0, 0, 0, 0, 0)