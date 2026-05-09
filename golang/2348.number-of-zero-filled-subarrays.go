func zeroFilledSubarray(nums []int) int64 {
	total, count := 0, 0

	for _, num := range nums {
		if num == 0 {
			count++
			total += count
		} else {
			count = 0
		}
	}

	return int64(total)
}
