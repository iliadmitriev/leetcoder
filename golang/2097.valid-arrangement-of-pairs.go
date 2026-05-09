func validArrangement(pairs [][]int) [][]int {
	adj := make(map[int][]int)
	ord := make(map[int]int)

	for _, p := range pairs {
		adj[p[0]] = append(adj[p[0]], p[1])
		ord[p[0]]--
		ord[p[1]]++
	}

	start := pairs[0][0]
	for k, v := range ord {
		if v == -1 {
			start = k
			break
		}
	}

	cur := start
	path := make([]int, 0, len(pairs))
	stack := make([]int, 0, len(pairs)+1)
	stack = append(stack, cur)

	for len(stack) > 0 {
		if len(adj[cur]) > 0 {
			stack = append(stack, cur)
			cur, adj[cur] = adj[cur][0], adj[cur][1:]
		} else {
			path = append(path, cur)
			cur = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
	}

	res := make([][]int, 0, len(path))
	for i := len(path) - 2; i >= 0; i-- {
		res = append(res, []int{path[i+1], path[i]})
	}

	return res
}
