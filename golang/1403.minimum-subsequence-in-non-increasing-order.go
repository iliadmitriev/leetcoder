import "sort"

func minSubsequence(nums []int) []int {
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))

	total, acc := 0, 0

	for i := 0; i < len(nums); i++ {
		total += nums[i]
	}

	for i := 0; i < len(nums); i++ {
		acc += nums[i]

		if 2*acc > total {
			return nums[:i+1]
		}
	}

	return nums
}
