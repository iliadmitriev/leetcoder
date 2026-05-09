class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        m, n = len(firstList), len(secondList)
        i, j = 0, 0
        res = []

        while i < m and j < n:
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            
            l, r = max(s1, s2), min(e1, e2)

            if r >= l:
                res.append([l, r])

            if e1 < e2:
                i += 1
            elif e1 > e2:
                j += 1
            else:
                i += 1
                j += 1

        return res
