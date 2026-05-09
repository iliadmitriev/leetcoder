import "sort"

func minimumOperations(nums []int) int {
	sort.Ints(nums)
	ops, shift := 0, 0

	for _, num := range nums {
		if num > shift {
			shift = num
			ops += 1
		}
	}

	return ops
}
