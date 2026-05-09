

from collections import deque


class Solution:
    def maxTaskAssign(
        self, tasks: list[int], workers: list[int], pills: int, strength: int
    ) -> int:
        """
        p = [1]
        t = [1, 2, 3]
        w = [0, 3, 3]

        p = [5]
        t = [5, 5, 8, 9, 9]
        w = [1, 2, 4, 6, 6]

        """
        n, m = len(tasks), len(workers)
        completed = 0

        def possible(k: int, tasks: list[int], workers: list[int], pills: int) -> bool:
            """
            k is the number of simplest tasks that can be completed with k strongest workers

            task index t: k - 1, 0

            worker index w: m - 1, m - k - 1

            """

            t = k - 1
            w = m - 1

            q = deque()

            while t >= 0:
                if not q and tasks[t] <= workers[w]:
                    t -= 1
                    w -= 1
                    continue

                if q and tasks[t] <= q[0]:
                    q.popleft()
                    t -= 1
                    continue

                while w >= m - k and workers[w] + strength >= tasks[t]:
                    q.append(workers[w])
                    w -= 1

                if q and pills > 0:
                    q.pop()
                    pills -= 1
                    t -= 1
                    continue

                return False

            return True

        tasks.sort()
        workers.sort()

        lo, hi = 0, min(n, m) + 1

        while lo < hi:
            mid = (lo + hi) // 2

            if possible(mid, tasks, workers, pills):
                lo = mid + 1
                completed = mid
            else:
                hi = mid

        return completed

