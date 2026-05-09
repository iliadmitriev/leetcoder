
func findTheArrayConcVal(nums []int) int64 {
	res := 0
	i, j := 0, len(nums)-1

	for i < j {
		res += concat(nums[i], nums[j])

		i++
		j--
	}

	if i == j {
		res += nums[i]
	}

	return int64(res)
}

func concat(a, b int) int {
	c := b

	for b > 0 {
		a *= 10
		b /= 10
	}

	return a + c
}
