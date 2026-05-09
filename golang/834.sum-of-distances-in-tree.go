package main

type Pair struct {
	node, parent int
}

type Node struct {
	node, parent int
	done         bool
}

func sumOfDistancesInTree(n int, edges [][]int) []int {
	sum, cnt := make([]int, n), make([]int, n)
	for i := range cnt {
		cnt[i] = 1
	}
	adj := make([][]int, n)
	for _, e := range edges {
		adj[e[0]] = append(adj[e[0]], e[1])
		adj[e[1]] = append(adj[e[1]], e[0])
	}

	st := make([]Node, 0, n)
	st = append(st, Node{0, -1, false})
	for len(st) > 0 {
		node := st[len(st)-1]
		st = st[:len(st)-1]

		if node.done {
			if node.parent == -1 {
				continue
			}
			cnt[node.parent] += cnt[node.node]
			sum[node.parent] += sum[node.node] + cnt[node.node]
		} else {
			node.done = true
			st = append(st, node)

			for _, ch := range adj[node.node] {
				if ch == node.parent {
					continue
				}
				st = append(st, Node{ch, node.node, false})
			}
		}
	}

	st2 := make([]Pair, 0, n)
	st2 = append(st2, Pair{0, -1})
	for len(st2) > 0 {
		node := st2[len(st2)-1]
		st2 = st2[:len(st2)-1]

		for _, ch := range adj[node.node] {
			if ch == node.parent {
				continue
			}
			sum[ch] = sum[node.node] - cnt[ch] + n - cnt[ch]
			st2 = append(st2, Pair{ch, node.node})
		}
	}
	return sum
}
