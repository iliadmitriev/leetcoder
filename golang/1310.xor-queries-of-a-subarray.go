func xorQueries(arr []int, queries [][]int) []int {
	n, m := len(arr), len(queries)
	prefix := make([]int, n+1)
	res := make([]int, m)

	for i := 1; i <= n; i++ {
		prefix[i] = prefix[i-1] ^ arr[i-1]
	}

	for j := 0; j < m; j++ {
		u, v := queries[j][0], queries[j][1]+1
		res[j] = prefix[u] ^ prefix[v]
	}

	return res
}
