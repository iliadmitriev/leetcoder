
func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}

	return a
}

func minOperations(nums []int) int {
	n := len(nums)
	cnt1 := 0
	for _, num := range nums {
		if num == 1 {
			cnt1++
		}
	}

	if cnt1 > 0 {
		return n - cnt1
	}

	var g int

	for d := 2; d <= n; d++ {
		for j := range n - d + 1 {
			g = gcd(nums[j], nums[j+1])
			nums[j] = g

			if g == 1 {
				return d + n - 2
			}
		}
	}

	return -1
}
