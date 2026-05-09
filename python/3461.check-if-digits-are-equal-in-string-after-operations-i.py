import collections


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        v1 = v2 = 0
        c = 1
        v = [ord(ch) - 48 for ch in s]
        n = len(v)

        for i in range(n):
            v1 = (v1 + v[i] * c) % 10
            v2 = (v2 + v[n - 1 - i] * c) % 10

            c = c * (n - 1 - i - 2) // (i + 1)

        return (v1 - v2) % 10 == 0

        q = collections.deque(map(int, s))

        while len(q) > 2:
            prev = q.popleft()
            for _ in range(len(q)):
                cur = q.popleft()

                q.append((cur + prev) % 10)
                prev = cur

        return q.pop() == q.popleft()

