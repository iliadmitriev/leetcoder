func countCompleteSubarrays(nums []int) int {
	n := len(nums)
	total, cur, size := 0, 0, 0
	maxValue := 0

	for _, num := range nums {
		maxValue = max(maxValue, num)
	}

	counter, win := make([]int, maxValue+1), make([]int, maxValue+1)

	for _, num := range nums {
		counter[num]++
		if counter[num] == 1 {
			size++
		}
	}

	for left, right := 0, 0; right < n; right++ {
		win[nums[right]]++
		if win[nums[right]] == 1 {
			cur++
		}

		for cur == size {
			win[nums[left]]--
			if win[nums[left]] == 0 {
				cur--
			}
			left++
		}

		total += left
	}

	return total
}
