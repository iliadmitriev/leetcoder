class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cache = {}
        res = []
        for num in nums:
            row = cache.get(num, -1) + 1

            while row >= len(res):
                res.append([])
            
            res[row].append(num)
            cache[num] = row

        return res