func mincostTickets(days []int, costs []int) int {
	sort.Ints(days)
	lastDay := days[len(days)-1]
	dp := make([]int, lastDay+1)

	for curDay, trip := 1, 0; curDay <= lastDay; curDay++ {
		if curDay < days[trip] {
			// if current day is covered by previous trip payment
			dp[curDay] = dp[curDay-1]
		} else {
			trip++
			dp[curDay] = min(
				dp[max(0, curDay-1)]+costs[0],
				min(
					dp[max(0, curDay-7)]+costs[1],
					dp[max(0, curDay-30)]+costs[2],
				),
			)
		}
	}

	return dp[lastDay]
}
