import (
	"slices"
)

func maxTotalValue(nums []int, k int) int64 {
	return int64(k) * int64(slices.Max(nums) - slices.Min(nums))
}