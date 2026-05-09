func maximumProduct(nums []int) int {
	sort.Ints(nums[:3])

	max1, max2, max3 := nums[2], nums[1], nums[0]
	min1, min2 := nums[0], nums[1]

	for _, num := range nums[3:] {
		if num > max1 {
			max3 = max2
			max2 = max1
			max1 = num
		} else if num > max2 {
			max3 = max2
			max2 = num
		} else if num > max3 {
			max3 = num
		}

		if num < min1 {
			min2 = min1
			min1 = num
		} else if num < min2 {
			min2 = num
		}
	}

	return max(
		min1*min2*max1,
		max1*max2*max3,
	)
}
