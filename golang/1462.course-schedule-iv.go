func checkIfPrerequisite(numCourses int, prerequisites [][]int, queries [][]int) []bool {
	N := len(queries)
	res := make([]bool, N)
	adj := make([][]int, numCourses)
	pre := make([]map[int]bool, numCourses)
	inDegree := make([]int, numCourses)
	q := make([]int, 0, numCourses)

	for _, p := range prerequisites {
		adj[p[0]] = append(adj[p[0]], p[1])
		inDegree[p[1]]++
	}

	for node := 0; node < numCourses; node++ {
		pre[node] = make(map[int]bool)
		if inDegree[node] == 0 {
			q = append(q, node)
		}
	}

	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		for _, nnode := range adj[node] {
			pre[nnode][node] = true
			for k := range pre[node] {
				pre[nnode][k] = true
			}

			inDegree[nnode]--
			if inDegree[nnode] == 0 {
				q = append(q, nnode)
			}
		}
	}

	for i, q := range queries {
		res[i] = pre[q[1]][q[0]]
	}

	return res
}
