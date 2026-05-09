import "sort"

func largestSumAfterKNegations(nums []int, k int) int {
	n := len(nums)
	sort.Slice(nums, func(i, j int) bool {
		return __absVal(nums[i]) > __absVal(nums[j])
	})

	for i := 0; i < n && k > 0; i++ {
		if nums[i] < 0 {
			nums[i] = -nums[i]
			k--
		}
	}

	if k%2 == 1 {
		nums[n-1] = -nums[n-1]
	}

	total := 0
	for _, v := range nums {
		total += v
	}

	return total
}

func __absVal(x int) int {
	if x < 0 {
		return -x
	}

	return x
}
