class Solution:
    def kMirror(self, k: int, n: int) -> int:
        total = 0
        count = 0

        def isPalindrome(v: int, k: int) -> bool:
            s = []
            while v > 0:
                s.append(v % k)
                v //= k
            return s == s[::-1]

        def mirror(n: int, odd: bool) -> int:
            m = n
            v = n if odd else n // 10
            while v:
                m = m * 10 + v % 10
                v //= 10
            return m

        prv = 1

        while count < n:
            nxt = 10 * prv

            for odd in [False, True]:
                for num in range(prv, nxt):
                    if count == n:
                        return total

                    value = mirror(num, odd)

                    if isPalindrome(value, k):
                        total += value
                        count += 1

            prv = nxt

        return total

