class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        @cache
        def dp(n: int) -> List[str]:
            
            # dp(0) = ''
            if n == 0:
                return ['']
            
            res = []
            # dp(n) = { dp(0) .. dp(n - 1) }({ dp(n - 1) .. dp(0) })
            for i in range(n):
                for left in dp( i ): # iterate all { dp(0) .. dp(n - 1) }
                    for right in dp(n - i - 1): # itreate all { dp(n - 1) .. dp(0) }
                        res.append(f'{left}({right})')
            return res
        
        return dp(n)