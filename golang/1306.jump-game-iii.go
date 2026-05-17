func canReach(arr []int, start int) bool {
	n := len(arr)
	vis := make([]bool, n)

	q := make([]int, 0, n)
	q = append(q, start)

	for len(q) > 0 {
		node := q[0]
		q = q[1:]

		if arr[node] == 0 {
			return true
		}

		for _, child := range []int{node + arr[node], node - arr[node]} {
			if child < 0 || n <= child || vis[child] {
				continue
			}

			vis[child] = true
			q = append(q, child)
		}
	}

	return false
}
    