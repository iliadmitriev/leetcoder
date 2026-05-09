import (
	"sort"
)

func maximumBeauty(nums []int, k int) int {
	sort.Ints(nums)

	left, n := 0, len(nums)
	maxLen := 0

	k *= 2

	for right := 0; right < n; right++ {
		for nums[right]-nums[left] > k {
			left++
		}

		if right-left+1 > maxLen {
			maxLen = right - left + 1
		}
	}

	return maxLen
}
