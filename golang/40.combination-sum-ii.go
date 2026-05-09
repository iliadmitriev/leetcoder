func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)

	res := [][]int{}
	path := []int{}
	combinationSum2Backtrack(candidates, target, 0, &path, &res)

	return res
}

func combinationSum2Backtrack(candidates []int, target, start int, path *[]int, res *[][]int) {
	if target < 0 {
		return
	}

	if target == 0 {
		finalPath := make([]int, len(*path))
		copy(finalPath, *path)

		*res = append(*res, finalPath)
		return
	}

	for i := start; i < len(candidates); i++ {
		if i > start && candidates[i] == candidates[i-1] {
			continue
		}

		*path = append(*path, candidates[i])
		combinationSum2Backtrack(candidates, target-candidates[i], i+1, path, res)
		*path = (*path)[:len(*path)-1]
	}
}
