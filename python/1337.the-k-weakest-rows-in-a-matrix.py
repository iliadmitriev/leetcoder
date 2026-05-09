from heapq import heapify, nsmallest


def get_zero(row: list) -> int:
    lo, hi = 0, len(row)
    while lo < hi:
        mid = (lo + hi) // 2
        if row[mid] == 0:
            hi = mid
        else:
            lo = mid + 1
    return lo


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i, row in enumerate(mat):
            res.append((get_zero(row), i))

        heapify(res)
        print(res)
        res = nsmallest(k, res)
        return list(map(lambda x: x[1], res))
        