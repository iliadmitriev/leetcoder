func partitionLabels(s string) []int {
	n := len(s)
	last := map[byte]int{}
	res := []int{}
	cur := 0
	end := 0

	for i := range n {
		last[s[i]] = i
	}

	for i := range n {
		end = max(end, last[s[i]])
		cur++

		if i == end {
			res = append(res, cur)
			cur = 0
		}
	}

	return res
}