class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        m, n = len(image), len(image[0])
        old_color = image[sr][sc]
        if old_color != color:
            q.append((sr, sc))
            image[sr][sc] = color
        steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while q:
            r, c = q.popleft()
            for dy, dx in steps:
                nr, nc = r + dy, c + dx
                if (0 <= nr < m and 0 <= nc < n and image[nr][nc] == old_color):
                    q.append((nr, nc))
                    image[nr][nc] = color
        return image