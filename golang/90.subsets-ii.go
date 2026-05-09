func dfsGenUnique(nums []int, path *[]int, i int, res *[][]int) {
	path_copy := make([]int, len(*path))
	copy(path_copy, *path)
	*res = append(*res, path_copy)

	for j := i; j < len(nums); j++ {
		if j > i && nums[j] == nums[j-1] {
			continue
		}

		*path = append(*path, nums[j])
		dfsGenUnique(nums, path, j+1, res)
		*path = (*path)[:len(*path)-1]
	}
}

func subsetsWithDup(nums []int) [][]int {
	n := len(nums)
	path := make([]int, 0, n)
	res := make([][]int, 0)

	sort.Ints(nums)

	dfsGenUnique(nums, &path, 0, &res)
	fmt.Println(len(res))
	return res
}
