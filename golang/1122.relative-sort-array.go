func relativeSortArray(arr1 []int, arr2 []int) []int {
	order := make(map[int]int, len(arr2))
	for i, v := range arr2 {
		order[v] = i
	}

	sort.Slice(arr1, func(i, j int) bool {
		a, b := arr1[i], arr1[j]
		pos_a, pos_b := a+len(arr1), b+len(arr1)
		if v, ok := order[a]; ok {
			pos_a = v
		}
		if v, ok := order[b]; ok {
			pos_b = v
		}

		return pos_a < pos_b
	})

	return arr1
}
