class Solution:
    def rotateGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        R = len(grid)
        C = len(grid[0])  # number of rows and columns
        L = min(R, C) // 2  # number of layers

        for d in range(L):  # d - layer number from 0 to L - 1
            si, ei = d, R - d - 1  # start and end of row indices
            sj, ej = d, C - d - 1  # start and end of column indices
            h, w = R - 2 * d, C - 2 * d  # height and width
            p = 2 * (h + w - 2)  # perimeter for current layer

            layer = []  # buffer for perimeter values

            # Extract the layer elements in counter-clockwise order:
            # top edge (left → right, excluding last corner)
            for j in range(w - 1):
                layer.append(grid[si][sj + j])
            # right edge (top → bottom, excluding last corner)
            for i in range(h - 1):
                layer.append(grid[si + i][ej])
            # bottom edge (right → left, excluding last corner)
            for j in range(w - 1):
                layer.append(grid[ei][ej - j])
            # left edge (bottom → top, excluding last corner)
            for i in range(h - 1):
                layer.append(grid[ei - i][sj])

            # Calculate starting index after rotation
            idx = k % p

            # Place elements back in the same order, starting from rotated position
            for j in range(w - 1):
                grid[si][sj + j] = layer[idx]
                idx = (idx + 1) % p

            for i in range(h - 1):
                grid[si + i][ej] = layer[idx]
                idx = (idx + 1) % p

            for j in range(w - 1):
                grid[ei][ej - j] = layer[idx]
                idx = (idx + 1) % p

            for i in range(h - 1):
                grid[ei - i][sj] = layer[idx]
                idx = (idx + 1) % p

        return grid
