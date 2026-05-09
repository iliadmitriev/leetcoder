import "sort"

func duplicateNumbersXOR(nums []int) int {
	res := 0

	sort.Ints(nums)
	for i := 1; i < len(nums); i++ {
		if nums[i-1] == nums[i] {
			res ^= nums[i]
		}
	}

	return res
}
