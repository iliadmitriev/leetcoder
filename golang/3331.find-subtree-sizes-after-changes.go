func findSubtreeSizes(parent []int, s string) []int {
	n := len(parent)
	adj := make([][]int, n)
	for v := 1; v < n; v++ {
		adj[parent[v]] = append(adj[parent[v]], v)
	}

	sizes := make([]int, n)
	for i := range n { // base: the node itself
		sizes[i] = 1
	}
	last := [26]int{}
	for i := range last {
		last[i] = -1
	}

	var dfs func(int)
	dfs = func(v int) {
		label := s[v] - 'a' // the label of the node v
		anc := last[label]  // preserve the ancestor of the node v with the same label

		last[label] = v            // set the new ancestor for the label
		for _, u := range adj[v] { // run children nodes with new label ancestor
			dfs(u)
		}
		last[label] = anc // revert the ancestor for the label

		// if node has no parent (root)
		if v <= 0 {
			return
		}

		// append sizes to the same label ancestor
		// or to the parent (if ancestor does not exist)
		p := parent[v]
		if anc >= 0 {
			p = anc
		}

		sizes[p] += sizes[v]
	}

	dfs(0)

	return sizes
}