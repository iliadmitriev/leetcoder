func findMaxLength(nums []int) int {
	cnt := 0
	res := 0
	dp := map[int]int{0: -1}

	for i, num := range nums {
		if num == 0 {
			cnt--
		} else {
			cnt++
		}

		if j, ok := dp[cnt]; ok {
			res = max(res, i-j)
		} else {
			dp[cnt] = i
		}
	}

	return res
}
