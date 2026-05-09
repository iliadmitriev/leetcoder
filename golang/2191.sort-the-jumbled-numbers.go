func sortJumbled(mapping []int, nums []int) []int {
	n := len(nums)
	tmp := make([][2]int, 0, n)

	for i := 0; i < n; i++ {
		tmp = append(tmp, [2]int{mapper(nums[i], mapping), i})
	}

	sort.Slice(tmp, func(i, j int) bool {
		return tmp[i][0] < tmp[j][0] || (tmp[i][0] == tmp[j][0] && tmp[i][1] < tmp[j][1])
	})

	res := make([]int, n)
	for i := 0; i < n; i++ {
		res[i] = nums[tmp[i][1]]
	}

	return res
}

func mapper(num int, mapping []int) int {
	if num == 0 {
		return mapping[0]
	}

	res := 0
	for place := 1; num > 0; place *= 10 {
		res += place * mapping[num%10]
		num /= 10
	}

	return res
}
