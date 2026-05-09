import (
	"sort"
)

func minimumDifference(nums []int, k int) int {
	if k < 2 {
		return 0
	}
  k--

	sort.Ints(nums)
	minDiff := nums[k] - nums[0]

	for i := k; i < len(nums); i++ {
		lo := nums[i-k]
		hi := nums[i]

		minDiff = min(minDiff, hi-lo)
	}

	return minDiff
}