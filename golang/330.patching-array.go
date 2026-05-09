func minPatches(nums []int, n int) int {
	cover := 0
	i := 0
	patches := 0

	for cover < n {
		if i == len(nums) || nums[i] > cover+1 {
			cover += cover + 1
			patches++
		} else {
			cover += nums[i]
			i++
		}
	}

	return patches
}
