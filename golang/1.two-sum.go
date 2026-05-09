func twoSum(nums []int, target int) []int {
	ch := make(map[int]int)
	res := []int{}
	for i, num := range nums {
		if j, ok := ch[target-num]; ok {
			res = append(res, i, j)
		}
    ch[num] = i
	}

	return res
}