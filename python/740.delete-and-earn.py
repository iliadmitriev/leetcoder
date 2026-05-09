class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        
        f(0) = 0
        f(1) = max( f(0) , data[1] * count(1) )
        ....
        f(n) = max( f(n - 1), data[n] * count(n) + f(n - 2))        
        """
        data = collections.Counter(nums)
        max_num = max(nums)
        for k in data.keys():
            data[k] *= k

        @cache
        def dp(num: int) -> int:
            if num == 0:
                return 0
            if num == 1:
                return data[1]
            
            return max(dp(num - 1), dp(num - 2) + data.get(num, 0))
        
        return dp(max_num)