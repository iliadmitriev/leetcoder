func findChampion(n int, edges [][]int) int {
	inorder := make([]int, n)
	m := len(edges)
	for i := 0; i < m; i++ {
		inorder[edges[i][1]]++
	}

	candidate := -1
	for u := 0; u < n; u++ {
		if inorder[u] > 0 {
			continue
		}

		if candidate == -1 {
			candidate = u
		} else {
			return -1
		}
	}

	return candidate
}
