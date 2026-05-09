import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """Finds minimum effort path on 2D grid.
        
        Idea:
            Use Dijkstra algorithm with Priority Queue (Heap Queue). Iterate all cell on the grid
            calculating effort (maximum absolute diffefence in heights) and finding minimal path.
            
        Algorithm:
            1) Init priority queue (effort, row, col) with start point
            2) Init best efforts matrix with infinite values (except for the start)
            2) Repat while priority queue is not empty
                * pop from top of queue another point
                * check if it's our target point (destination), then return it's effort
                * mark cell as visited
                * iterate all four directions of adjacent cells
                    + check if it's a valid cell (didn't step off the grid) and
                      it's not visited yet
                        - calculate effort of cell (maximum absolute difference)
                        - if it's a best effort (less than corresponding cell in best matrinx)
                          add it to the best matrix and to the queue
        
        Args:
            heights (list of list of int): input 2D matrix of representing heights of each cell
            
        Returns:
            (int): minimum effort required to travel from top-left to bottom-right cell.
        """
        rows, cols = len(heights), len(heights[0])
        # min heap proirity queue, with starting point of 0 effort, and 0, 0 - coordinates
        hq = [(0, 0, 0)]
        # init best efforts
        best = [[float('inf')] * cols for _ in range(rows)]
        best[0][0] = 0

        # possible directions
        dirs = ((-1, 0), (0, -1), (0, 1), (1, 0))

        while hq:
            effort, row, col = heapq.heappop(hq)

            if (row, col) == (rows - 1, cols - 1):
                return effort

            for drow, dcol in dirs:
                nrow, ncol = row + drow, col + dcol
                if 0 <= nrow < rows and 0 <= ncol < cols:
                    neffort = max(effort, abs(heights[row][col] - heights[nrow][ncol]))
                    if neffort < best[nrow][ncol]:
                        best[nrow][ncol] = neffort
                        heapq.heappush(hq, (neffort, nrow, ncol))


            

