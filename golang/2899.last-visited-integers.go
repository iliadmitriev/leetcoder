func lastVisitedIntegers(nums []int) []int {
	k := 0
	ans, seen := make([]int, 0), make([]int, 0)

	for _, num := range nums {
		if num > 0 {
			seen = append(seen, num)
			k = 0
		} else {
			if len(seen)-k > 0 {
				ans = append(ans, seen[len(seen)-k-1])
				k++
			} else {
				ans = append(ans, -1)
			}
		}
	}

	return ans
}
