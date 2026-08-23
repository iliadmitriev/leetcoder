class Solution:
    def sumGame(self, num: str) -> bool:
        def get(i: int, j: int) -> tuple[int, int]:
            n, q = 0, 0
            base = ord("0")

            for k in range(i, j):
                if num[k] == "?":
                    q += 1
                else:
                    n += ord(num[k]) - base

            return n, q

        n = len(num)

        n0, q0 = get(0, n // 2)
        n1, q1 = get(n // 2, n)

        return (q0 + q1) % 2 == 1 or n0 - n1 != (q1 - q0) * 9 // 2