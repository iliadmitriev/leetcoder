import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        if "*" not in s:
            return s

        pq = []
        res = [""] * len(s)

        for i, c in enumerate(s):
            if c == "*":
                _, j = heapq.heappop(pq)
                res[-j] = ""
            else:
                res[i] = c
                heapq.heappush(pq, (ord(c), -i))

        return "".join(res)

