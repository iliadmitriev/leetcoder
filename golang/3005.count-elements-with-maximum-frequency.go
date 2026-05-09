func maxFrequencyElements(nums []int) int {
	cnt := make([]int, 101)
	for _, nums := range nums {
		cnt[nums]++
	}

	m := 0
	for _, c := range cnt {
		if c > m {
			m = c
		}
	}

	res := 0
	for _, c := range cnt {
		if c == m {
			res += c
		}
	}

	return res
}
