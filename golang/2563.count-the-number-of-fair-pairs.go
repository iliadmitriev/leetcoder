import "sort"

func countFairPairs(nums []int, lower int, upper int) int64 {
	sort.Ints(nums)

	// count all pairs strictly greater than upper bound + 1
	hi := countPairsLowerThanBound(nums, upper+1)

	// count all pairs strictly less than lower bound
	lo := countPairsLowerThanBound(nums, lower)

	count := hi - lo

	return int64(count)
}

// binSearchLow - binary search target insert position with lower bound
func countPairsLowerThanBound(arr []int, bound int) int {
	left, right := 0, len(arr)-1
	count := 0
	var sum int

	for left < right {
		sum = arr[left] + arr[right]

		if sum < bound {
			count += right - left
			left++
		} else {
			right--
		}
	}

	return count
}
