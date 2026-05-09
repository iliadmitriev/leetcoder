class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n + 1)

        for i in range(len(ranges)):
            start, end = max(0, i - ranges[i]), min(n, i + ranges[i])
            max_reach[start] = max(max_reach[start], end)
        
        taps = 0
        cur_end = 0
        max_end = 0

        for i in range(n + 1):
            if max_end < i:
                return -1

            if cur_end < i:
                taps += 1
                cur_end = max_end

            if max_end < max_reach[i]:
                max_end = max_reach[i]

        return taps