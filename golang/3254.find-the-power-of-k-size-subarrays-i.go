func resultsArray(nums []int, k int) []int {
	if k == 1 {
		return nums
	}

	n := len(nums)
	counter := 1
	res := make([]int, 0, n-k+1)

	for i := 1; i < n; i++ {
		if nums[i-1]+1 == nums[i] {
			counter++
		}

		if i >= k {
			if nums[i-k]+1 == nums[i-k+1] {
				counter--
			}
		}

		if i+1 >= k {
			if counter == k {
				res = append(res, nums[i])
			} else {
				res = append(res, -1)
			}
		}
	}

	return res
}
