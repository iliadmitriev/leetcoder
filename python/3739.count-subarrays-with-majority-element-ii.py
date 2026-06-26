class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        res = 0

        # shifted current running prefix [-n;n] -> [1;2*n+1]
        pre = n + 1 # n + 1 is a real 0 
        cnt = [0] * (2 * n + 2) # prefix frequency
        acc = [0] * (2 * n + 2) # prefix accumulated frequency

        cnt[pre] = 1 # cnt[0] = 1
        acc[pre] = 1 # acc[0] = 1

        for num in nums:
            # update runnung prefix
            if target == num:
                pre += 1
            else:
                pre -= 1
                
            # update running prefix frequency
            cnt[pre] += 1

            # recalculate current prefix accumulated frequency
            # use accumulated frequnecy of prefix of previous length
            # add current prefix count
            acc[pre] = acc[pre - 1] + cnt[pre]

            # not inclusive (previous prefix)
            res += acc[pre - 1]

        return res
        