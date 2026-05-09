func maximumLength(nums []int) int {
	odd, even, alter1, alter2 := 0, 0, 0, 0

	for _, num := range nums {
		if num%2 == 0 {
			even++
			alter1 = 1 + alter2
		} else {
			odd++
			alter2 = 1 + alter1
		}
	}

	return max(
		max(even, odd),
		max(alter1, alter2),
	)
}
