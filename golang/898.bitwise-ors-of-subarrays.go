func subarrayBitwiseORs(arr []int) int {
	res := make(map[int]struct{})

	for i, x := range arr {
		skip := 0
		take := x

		res[x] = struct{}{}

		for j := i - 1; j >= 0; j-- {
			skip |= arr[j]
			take |= arr[j]

			if skip == take {
				break
			}

			res[take] = struct{}{}
		}
	}

	return len(res)
}
