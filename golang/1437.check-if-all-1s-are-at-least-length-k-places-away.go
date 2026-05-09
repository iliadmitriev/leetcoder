func kLengthApart(nums []int, k int) bool {
	distance := -1

	for _, num := range nums {
		if num == 1 {
			if distance > 0 {
				return false
			}
			distance = k
		} else {
			distance--
		}
	}

	return true
}
