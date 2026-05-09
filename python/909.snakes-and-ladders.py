import collections


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        m, n = len(board), len(board[0])
        start, finish = 1, m * n
        size = finish + 1

        b = [0] * size
        ltr = True
        i = 1
        for r in range(m - 1, -1, -1):
            if ltr:
                for c in range(n):
                    b[i] = board[r][c]
                    i += 1
            else:
                for c in range(n - 1, -1, -1):
                    b[i] = board[r][c]
                    i += 1

            ltr = not ltr

        q = collections.deque()
        q.append((start, 0))

        vis = [False] * size
        vis[start] = True

        while q:
            pos, move = q.popleft()

            # got to the end
            if pos == finish:
                return move

            # roll the dice to get 1 to 6 moves
            for i in range(6, 0, -1):
                npos = min(pos + i, finish)

                # snake or ladder move
                if b[npos] != -1:
                    npos = b[npos]

                if not vis[npos]:
                    vis[npos] = True
                    q.append((npos, move + 1))

        return -1

