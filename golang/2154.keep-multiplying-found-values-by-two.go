func findFinalValue(nums []int, original int) int {
	sort.Ints(nums)

	for _, v := range nums {
		if v == original {
			original *= 2
		}
	}

	return original
}
