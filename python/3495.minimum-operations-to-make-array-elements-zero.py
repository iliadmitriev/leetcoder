

class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        count = 0

        def counter(a: int, b: int) -> int:
            prev = 1
            i = 1
            total = 0

            while prev <= b:
                cur = 4 * prev
                left = max(a, prev)
                right = min(b, cur - 1)

                if left <= right:
                    total += (right - left + 1) * i

                prev = cur
                i += 1

            return (total + 1) // 2

        for a, b in queries:
            count += counter(a, b)

        return count

