class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x: x[1])
        n = len(pairs)
        length = 1  # it's guaranteed that we have one pair
        end = pairs[0][1]
        
        for i in range(1, n):
            if pairs[i][0] > end:
                length += 1
                end = pairs[i][1]

        return length