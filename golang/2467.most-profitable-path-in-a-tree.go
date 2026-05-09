func mostProfitablePath(edges [][]int, bob int, amount []int) int {
	N := len(amount)
	tree := make([][]int, N)
	adj := make([][]int, N)
	q := make([][2]int, 0, N)
	q1 := make([][2]int, 0, N)
	parent := make([]int, N)
	profit := math.MinInt

	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
		adj[e[1]] = append(adj[e[1]], e[0])
	}

	q1 = append(q1, [2]int{0, 0})
	for len(q1) > 0 {
		u, p := q1[0][0], q1[0][1]
		q1 = q1[1:]
		parent[u] = p

		for _, v := range adj[u] {
			if v == p {
				continue
			}

			q1 = append(q1, [2]int{v, u})
			tree[u] = append(tree[u], v)
		}
	}

	q = append(q, [2]int{0, 0})
	for len(q) > 0 {

		for m := len(q); m > 0; m-- {
			alice, curProfit := q[0][0], q[0][1]
			q = q[1:]

			curAmount := amount[alice]
			if alice == bob {
				curAmount /= 2
			}

			if len(tree[alice]) == 0 {
				profit = max(profit, curProfit+curAmount)
			}

			for _, child := range tree[alice] {
				q = append(q, [2]int{child, curProfit + curAmount})
			}
		}

		amount[bob] = 0
		bob = parent[bob]
	}

	return profit
}
