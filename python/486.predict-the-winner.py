class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def dp(p1: int, p2: int, nums: List[int]) -> bool:
            if len(nums) == 0:
                return p1 >= p2
            if len(nums) == 1:
                return p1 + nums[0] >= p2

            # returns first player move or second player move result
            return (
                dp(p1 + nums[0], p2 + nums[1], nums[2:]) and dp(p1 + nums[0], p2 + nums[-1], nums[1:-1])
            ) or (
                dp(p1 + nums[-1], p2 + nums[0], nums[1:-1]) and  dp(p1 + nums[-1], p2 + nums[-2], nums[:-2])
            )

        return dp(0, 0, nums)