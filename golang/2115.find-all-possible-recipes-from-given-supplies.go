func findAllRecipes(recipes []string, ingredients [][]string, supplies []string) []string {
	done := make([]string, 0)
	N, M := len(recipes), len(supplies)
	q := make([]string, 0, max(M, N))
	recipesSet := make(map[string]struct{}, N)
	adj := make(map[string][]string, N)
	inorder := make(map[string]int, N)

	for _, r := range recipes {
		recipesSet[r] = struct{}{}
	}

	for i := range N {
		for _, _from := range ingredients[i] {
			adj[_from] = append(adj[_from], recipes[i])
			inorder[recipes[i]]++
		}
	}

	for _, s := range supplies {
		q = append(q, s)
	}

	for len(q) > 0 {
		ing := q[0]
		q = q[1:]

		if _, ok := recipesSet[ing]; ok {
			done = append(done, ing)
		}

		for _, next := range adj[ing] {
			inorder[next]--

			if inorder[next] == 0 {
				q = append(q, next)
			}
		}
	}

	return done
}
