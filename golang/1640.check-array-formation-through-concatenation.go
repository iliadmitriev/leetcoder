func canFormArray(arr []int, pieces [][]int) bool {
	adj := make(map[int][]int)

	for _, p := range pieces {
		adj[p[0]] = p
	}

	if _, ok := adj[arr[0]]; !ok {
		return false
	}

	p := adj[arr[0]]
	for i, j := 0, 0; i < len(arr); i, j = i+1, j+1 {
		if j == len(p) {
			if _, ok := adj[arr[i]]; !ok {
				return false
			}

			p = adj[arr[i]]
			j = 0
		}

		if p[j] != arr[i] {
			return false
		}
	}

	return true
}
