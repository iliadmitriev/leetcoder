func largeGroupPositions(s string) [][]int {
	res := make([][]int, 0)
	n := len(s)

	for i, j := 0, 0; i < n; i = j {
		for j < n && s[i] == s[j] {
			j++
		}

		if j-i >= 3 {
			res = append(res, []int{i, j - 1})
		}
	}

	return res
}
