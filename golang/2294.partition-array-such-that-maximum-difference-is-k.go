import "sort"

func partitionArray(nums []int, k int) int {
	count := 1
	n := len(nums)

	sort.Ints(nums)

	for i, j := 0, 0; i < n; i++ {
		if nums[i]-nums[j] > k {
			count++
			j = i
		}
	}

	return count
}
