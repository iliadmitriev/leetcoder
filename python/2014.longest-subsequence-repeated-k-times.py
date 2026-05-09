import collections


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""

        letters = sorted(
            [c for c, f in collections.Counter(s).items() if f >= k], reverse=True
        )

        def check(s: str, p: str, k: int) -> bool:
            """Check if s is a subsequence of p."""

            it = iter(s)
            return all(ch in it for _ in range(k) for ch in p)

        q = collections.deque(letters)
        while q:
            cur = q.popleft()

            if len(cur) > len(ans):
                ans = cur

            for c in letters:
                nxt = cur + c
                if check(s, nxt, k):
                    q.append(nxt)

        return ans

