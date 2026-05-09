import "slices"

func maxFrequency(nums []int, k int, numOperations int) int {
	maxNum := slices.Max(nums)
	cnt := make([]int, maxNum+1)

	for _, num := range nums {
		cnt[num]++
	}

	// left : [num - k, num - 1]
	// right : [num + 1, num + k]
	left, right := 0, 0
	maxFreq := 0

	limit := min(k, maxNum+1)
	for i := range limit {
		right += cnt[i]
	}

	for num := range maxNum + 1 {
		right -= cnt[num]

		if num+k <= maxNum {
			right += cnt[num+k]
		}

		if num-1 >= 0 {
			left += cnt[num-1]
		}

		if num-k-1 >= 0 {
			left -= cnt[num-k-1]
		}

		maxFreq = max(maxFreq, cnt[num]+min(numOperations, right+left))
	}

	return maxFreq
}
