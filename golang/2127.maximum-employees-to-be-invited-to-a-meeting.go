func maximumInvitations(favorite []int) int {
	N := len(favorite)
	inDegree := make([]int, N)
	depth := make([]int, N)

	for node := 0; node < N; node++ {
		inDegree[favorite[node]]++
	}

	q := make([]int, 0, N)
	for node, d := range inDegree {
		if d == 0 {
			q = append(q, node)
		}
	}

	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		nnode := favorite[node]
		depth[nnode] = max(depth[nnode], depth[node]+1)
		inDegree[nnode]--
		if inDegree[nnode] == 0 {
			q = append(q, nnode)
		}
	}

	maxCycleLen, sumLenTwoCyclePath := 0, 0

	for node := 0; node < N; node++ {
		if inDegree[node] == 0 {
			continue
		}

		cycleLen := 0
		for cur := node; inDegree[cur] != 0; cur = favorite[cur] {
			inDegree[cur] = 0
			cycleLen++
		}

		if cycleLen == 2 {
			sumLenTwoCyclePath += depth[node] + depth[favorite[node]] + 2
		} else {
			maxCycleLen = max(maxCycleLen, cycleLen)
		}

	}

	return max(maxCycleLen, sumLenTwoCyclePath)
}
