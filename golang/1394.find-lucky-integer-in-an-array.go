func findLucky(arr []int) int {
	cnt := make([]int, 501)
	cnt[0] = -1

	for _, num := range arr {
		cnt[num]++
	}

	res := -1

	for k, v := range cnt {
		if k == v && k > res {
			res = k
		}
	}

	return res
}
