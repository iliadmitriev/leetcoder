class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = 0
        
        freq = Counter(nums)
        
        if k == 0:
            for v in freq.values():
                if v >= 2:
                    counter += 1
        else:
            for v in freq.keys():
                if v + k in freq:
                    counter += 1
        
        return counter