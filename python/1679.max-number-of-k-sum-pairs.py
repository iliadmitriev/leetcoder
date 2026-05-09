class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        res = 0
        for i in nums:
            if m[k - i] > 0:
                res += 1
                m[k - i] -= 1
            else:
                m[i] += 1
        
        return res