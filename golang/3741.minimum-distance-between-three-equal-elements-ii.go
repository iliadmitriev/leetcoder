func minimumDistance(nums []int) int {
	n := len(nums)
  if n < 3 {
    return -1
  }
  
	inf := 2*n + 1
	cache := make(map[int][]int, n)
	min_dist := inf

	for i, num := range nums {
		cache[num] = append(cache[num], i)

		if k := len(cache[num]); k >= 3 {
			min_dist = min(min_dist, 2*(cache[num][k-1]-cache[num][k-3]))

			if min_dist == 4 {
				return min_dist
			}
		}

	}

	if min_dist == inf {
		return -1
	}

	return min_dist
}