func minimumOperations(nums []int) int {
	res := 0

	for _, num := range nums {
		if num%3 != 0 {
			res++
		}
	}

	return res
}
