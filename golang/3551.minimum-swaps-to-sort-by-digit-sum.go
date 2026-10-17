func minSwaps(nums []int) int {

	sumDigits := func(x int) int {
		y := 0
		for x > 0 {
			y += x % 10
			x /= 10
		}
		return y
	}

	n := len(nums)
	arr := make([][3]int, 0, n)
	for i, x := range nums {
		arr = append(arr, [3]int{sumDigits(x), x, i})
	}

	slices.SortFunc(arr, func(a, b [3]int) int {
		if a[0] != b[0] {
			return a[0] - b[0]
		}
		if a[1] != b[1] {
			return a[1] - b[1]
		}
		return a[2] - b[2]
	})

	swaps := 0
	vis := make([]bool, n)

	for i := range n {
		// if it's already visited or it's on its own place -> skip
		if vis[i] || arr[i][2] == i {
			continue
		}

		j := i
		cycle := 0

		for !vis[j] {
			vis[j] = true
			j = arr[j][2]
			cycle++
		}

		swaps += cycle - 1
	}

	return swaps
}