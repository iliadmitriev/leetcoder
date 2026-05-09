class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        Time O(n**2)
        Space: O(n)
        
        nums[a] + nums[b] + nums[c] == nums[d]  =>  
        nums[a] + nums[b] == nums[d] - nums[c]
        """
        count = 0
        # cache nums[a] + nums[b]
        cache_d_c = defaultdict(int)
        n = len(nums)
        for a in range(n - 1, 0, -1):
            for b in range(a - 1, -1, -1):
                s = nums[a] + nums[b]
                if s in cache_d_c:
                    count += cache_d_c[s] 
            # now a plays role of d index
            for d in range(n - 1, a, -1):
                cache_d_c[nums[d] - nums[a]] += 1
        return count