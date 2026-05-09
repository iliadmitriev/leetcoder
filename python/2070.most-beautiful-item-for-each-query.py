class Solution:
    @staticmethod
    def binSearch(arr: list[tuple[int, int]], target: int) -> int:
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid][0] > target:
                hi = mid
            else:
                lo = mid + 1

        return lo

    def maximumBeauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        m = len(queries)
        results = [0] * m
        items.sort()
        data: list[tuple[int, int]] = [(0, 0)]

        for price, beauty in items:
            item = price, max(beauty, data[-1][1])
            if data[-1][0] == price:
                data[-1] = item
            else:
                data.append(item)

        for i, q in enumerate(queries):
            idx = self.binSearch(data, q)

            if idx > 0:
                idx -= 1
                results[i] = data[idx][1]

        return results

