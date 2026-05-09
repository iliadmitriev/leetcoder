func countStudents(students []int, sandwiches []int) int {
	cnt := [2]int{}

	for _, s := range students {
		cnt[s]++
	}

	for _, s := range sandwiches {
		if cnt[s] > 0 {
			cnt[s]--
		} else {
			break
		}
	}

	return cnt[0] + cnt[1]
}
