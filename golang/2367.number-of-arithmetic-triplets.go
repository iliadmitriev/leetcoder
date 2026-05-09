func arithmeticTriplets(nums []int, diff int) int {
	n := len(nums)

	count := 0

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if nums[j]-nums[i] != diff {
				continue
			}

			for k := j + 1; k < n; k++ {
				if nums[k]-nums[j] != diff {
					continue
				}
				count++
				break
			}

			break
		}
	}

	return count
}
