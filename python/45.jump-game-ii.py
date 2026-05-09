class Solution:
    def jump(self, nums: List[int]) -> int:
        # maximum possible jump from current index
        max_curr = 0
        # max reachable index for current jump
        curr_jump = 0
        # numer of jumsp
        jumps = 0

        for i in range(len(nums) - 1):
            max_curr = max(max_curr, i + nums[i])
            if curr_jump <= i:
                jumps += 1
                curr_jump = max_curr

        return jumps