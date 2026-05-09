func minHeightShelves(books [][]int, shelfWidth int) int {
	INF := int(1e9)
	n := len(books)
	dp := make([]int, n+1)

	for i := n - 1; i >= 0; i-- {
		w, h := 0, 0
		dp[i] = INF
		for j := i; j < n; j++ {
			w += books[j][0]
			h = max(h, books[j][1])
			if w > shelfWidth {
				break
			}

			dp[i] = min(dp[i], h+dp[j+1])
		}
	}

	return dp[0]
}
