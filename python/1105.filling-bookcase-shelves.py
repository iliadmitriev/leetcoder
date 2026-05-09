

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        INF = int(1e9)
        n = len(books)

        dp = [INF] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            w, h = 0, 0
            for j in range(i, n):
                w += books[j][0]
                h = max(h, books[j][1])
                if w > shelfWidth:
                    break
                dp[i] = min(dp[i], h + dp[j + 1])

        return dp[0]

