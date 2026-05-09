from collections import deque


class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        moves = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]

        finish = (1, 2, 3, 4, 5, 0)

        vis: set[tuple[int, ...]] = set()
        k = tuple(board[0] + board[1])
        start = k.index(0)
        vis.add(k)
        q = deque([(start, k)])
        step = 0

        while q:

            for _ in range(len(q)):
                pos, k = q.popleft()

                if k == finish:
                    return step

                for move in moves[pos]:
                    k_new = list(k)

                    k_new[pos], k_new[move] = k_new[move], k_new[pos]
                    k_next = tuple(k_new)

                    if k_next in vis:
                        continue

                    q.append((move, k_next))
                    vis.add(k_next)

            step += 1

        return -1

