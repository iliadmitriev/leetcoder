import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """Heap Queue solution."""
        m, n = len(matrix), len(matrix[0])
        # row indexes
        indexes = [0] * m
        # priority queue of tuples: (value, row_num)
        hq = []
        for i in range(m):
            heapq.heappush(hq, (matrix[i][indexes[i]], i))
        
        # init value
        val = matrix[0][0]
        for i in range(k):
            val, idx = heapq.heappop(hq)
            if indexes[idx] < n - 1:
                indexes[idx] += 1
                heapq.heappush(hq, (matrix[idx][indexes[idx]], idx))
            
        return val