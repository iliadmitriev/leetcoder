class Solution:
    def avgCells(self, y: int, x: int, arr: list[list[int]], l: int = 3) -> int:
        res, n = 0, 0
        for i in range(-(l // 2), l // 2 + l % 2):
            for j in range(-(l // 2), l // 2 + l % 2):
                if 0 <= y + i < len(arr) and 0 <= x + j < len(arr[y + i]):
                    n += 1
                    res += arr[y + i][x + j]
        return res // n
            
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        avg = self.avgCells
        return [[avg(i, j, img) for j in range(len(row))] for i, row in enumerate(img)]