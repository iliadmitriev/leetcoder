func construct2DArray(original []int, m int, n int) [][]int {
	if m*n != len(original) {
		return nil
	}

	res := make([][]int, m)
	for i := 0; i < m; i++ {
		res[i] = make([]int, n)
	}

	for i, value := range original {
		res[i/n][i%n] = value
	}

	return res
}
