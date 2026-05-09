func findShortestSubArray(nums []int) int {
	cache := make(map[int][]int) // num -> (start, end, count)
	degree := 1
	for i, num := range nums {
		if _, ok := cache[num]; ok {
			cache[num][1] = i
			cache[num][2]++
			degree = max(degree, cache[num][2])
		} else {
			cache[num] = []int{i, i, 1}
		}
	}

	minLength := len(nums)

	for _, v := range cache {
		if v[2] == degree {
			minLength = min(minLength, v[1]-v[0]+1)
		}
	}

	return minLength
}
