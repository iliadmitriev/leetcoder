func rowAndMaximumOnes(mat [][]int) []int {
	res := make([]int, 2)
	curRowCount := 0

	for i := 0; i < len(mat); i++ {
		curRowCount = accumulate(mat[i])
		if curRowCount > res[1] {
			res[0] = i
			res[1] = curRowCount
		}
	}

	return res
}

func accumulate(nums []int) int {
	res := 0
	for _, num := range nums {
		res += num
	}

	return res
}
