func binSearch(arr *[]int, target int) bool {
	lo, hi := 0, len(*arr)

	for lo < hi {
		mid := (lo + hi) / 2

		if (*arr)[mid] < target {
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	return lo < len(*arr) && (*arr)[lo] == target
}

func subsetBacktrack(nums []int, i, k int, path *[]int) int {
	if i >= len(nums) {
		if len(*path) > 0 {
			return 1
		} else {
			return 0
		}
	}

	res := 0
	if nums[i]-k < 0 || !binSearch(path, nums[i]-k) {
		*path = append(*path, nums[i])
		res += subsetBacktrack(nums, i+1, k, path)
		*path = (*path)[:len(*path)-1]
	}

	return res + subsetBacktrack(nums, i+1, k, path)
}

func beautifulSubsets(nums []int, k int) int {
	sort.Ints(nums)
	path := make([]int, 0, len(nums))
	return subsetBacktrack(nums, 0, k, &path)
}
