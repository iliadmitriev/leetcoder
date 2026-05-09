class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        n = len(nums)
        res = []
        
        def dfs(comb):
            if len(comb) == n:
                res.append(comb)
                
            else:
                for num in counter.keys():
                    if counter[num] > 0:

                        counter[num] -= 1
                        dfs(comb + [num])
                        counter[num] += 1
                        
        dfs([])
        
        return res