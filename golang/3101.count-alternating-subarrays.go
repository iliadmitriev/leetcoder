func countAlternatingSubarrays(nums []int) int64 {
	total := 0
	cur, curLen := -1, 0

	for _, num := range nums {

		if num == cur {
			curLen = 1
		} else {
			curLen++
		}

		total += curLen
		cur = num
	}

	return int64(total)
}
