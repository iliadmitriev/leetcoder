import collections


class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        q = collections.deque(nums)
        res = []

        while len(q) > 1:
            a = q.popleft()
            b = q.popleft()

            if gcd(a, b) == 1:
                res.append(a)
                q.appendleft(b)
            else:
                c = lcm(a, b)

                while res and gcd(c, res[-1]) > 1:
                    c = lcm(c, res.pop())

                q.appendleft(c)

        if q:
            res.append(q.popleft())

        return res

