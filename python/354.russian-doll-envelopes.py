class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        res = []
        for _, x in envelopes:
                
            idx = bisect_left(res, x)
            if idx == len(res):
                res.append(x)
            else:
                res[idx] = x
            
        return len(res)