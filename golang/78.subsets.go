
func subsets(nums []int) [][]int {
	n := len(nums)
	res := make([][]int, 0, 1<<n)
	res = append(res, []int{})

	for _, num := range nums {
		m := len(res)
		for i := 0; i < m; i++ {
			tmp := make([]int, len(res[i]), len(res[i])+1)
			copy(tmp, res[i])
			tmp = append(tmp, num)

			res = append(res, tmp)
		}
	}

	return res
}
