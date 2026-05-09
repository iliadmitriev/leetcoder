func separateDigits(nums []int) []int {
	res := make([]int, 0)

	for i := len(nums) - 1; i >= 0; i-- {
		num := nums[i]

		for num > 0 {
			res = append(res, num%10)
			num /= 10
		}
	}

	slices.Reverse(res)
	return res
}
