import "sort"

func maximumStrongPairXor(nums []int) int {
	res := 0
	n := len(nums)

	sort.Ints(nums)

	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if nums[j] > 2*nums[i] {
				break
			}

			res = max(res, nums[i]^nums[j])
		}
	}

	return res
}
