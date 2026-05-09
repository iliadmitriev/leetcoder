func findRelativeRanks(score []int) []string {
	n := len(score)
	places := make([]int, n)
	for i := 0; i < n; i++ {
		places[i] = i
	}

	sort.Slice(places, func(i, j int) bool {
		return score[places[i]] > score[places[j]]
	})

	res := make([]string, n)
	for i := 0; i < n; i++ {
		res[places[i]] = strconv.Itoa(i + 1)
	}

	prize := map[int]string{0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
	for i := 0; i < min(3, n); i++ {
		res[places[i]] = prize[i]
	}

	return res
}
