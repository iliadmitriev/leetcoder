import "sort"

func maxValue(events [][]int, k int) int {
	n := len(events)

	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, k+1)
	}

	// sort events by start time
	sort.Slice(events, func(i, j int) bool {
		return events[i][0] < events[j][0]
	})

	for i := n - 1; i >= 0; i-- {
		// next index where current event end time is is less than next event start time
		idx := bisertRightIndex(i, n, func(m int) bool {
			return events[i][1] < events[m][0]
		})

		for j := 1; j <= k; j++ {
			dp[i][j] = max(dp[i+1][j], dp[idx][j-1]+events[i][2])
		}
	}

	return dp[0][k]
}

func bisertRightIndex(lo, hi int, cmp func(int) bool) int {
	var mid int
	for lo < hi {
		mid = lo + (hi-lo)/2

		if cmp(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}
