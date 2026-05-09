func buildMatrix(k int, rowConditions [][]int, colConditions [][]int) [][]int {
	rows, cols := topologicalSort(k, rowConditions), topologicalSort(k, colConditions)
	if len(rows) == 0 || len(cols) == 0 {
		return nil
	}

	mat := make([][]int, k)
	for i := 0; i < k; i++ {
		mat[i] = make([]int, k)
	}

	for i := 0; i < k; i++ {
		mat[rows[i]][cols[i]] = i + 1
	}

	return mat
}

func topologicalSort(n int, edges [][]int) []int {
	adj := make([][]int, n)
	inorder := make([]int, n)
	order := make([]int, n)

	for _, edge := range edges {
		adj[edge[0]-1] = append(adj[edge[0]-1], edge[1]-1)
		inorder[edge[1]-1]++
	}

	q := make([]int, 0, n)
	for i := 0; i < n; i++ {
		if inorder[i] == 0 {
			q = append(q, i)
		}
	}

	j := 0
	for len(q) > 0 {
		u := q[0]
		q = q[1:]

		order[u] = j
		j++

		for _, v := range adj[u] {
			inorder[v]--
			if inorder[v] == 0 {
				q = append(q, v)
			}
		}
	}

	if j != n {
		return nil
	}

	return order
}
