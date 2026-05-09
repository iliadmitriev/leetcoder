class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        idx = []
        cnt = []
        count = 0
        for i, ch in enumerate(s):
            if ch == '|':
                idx.append(i)
                cnt.append(count)
                count = 0
            elif ch == '*':
                count += 1

        data = list(accumulate(cnt))

        res = []
        for q1, q2 in queries:
            l = bisect_left(idx, q1)
            r = bisect_right(idx, q2)
            if l < len(idx) and r - 1 < len(idx) and l != r:
                res.append(data[r - 1] - data[l])
            else:
                res.append(0)

        return res