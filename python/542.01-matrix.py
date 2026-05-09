class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return mat

        m, n = len(mat), len(mat[0])
        queue = deque()
        MAX = m * n # +inf

        # add start values to queue, 
        # and mark not visited values as +inf
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = MAX

        # set directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                # if value of new cell wich we take a step
                # is greater than current cell value + 1
                # then it should be updated
                if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
                    queue.append((r, c))
                    mat[r][c] = mat[row][col] + 1

        return mat