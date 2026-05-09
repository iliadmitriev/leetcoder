func timeRequiredToBuy(tickets []int, k int) int {
	t := 0
	top := tickets[k]

	for i := 0; i < len(tickets); i++ {
		if i <= k {
			t += min(top, tickets[i])
		} else {
			t += min(top-1, tickets[i])
		}
	}

	return t
}
