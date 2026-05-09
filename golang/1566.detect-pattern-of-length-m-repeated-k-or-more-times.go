func containsPattern(arr []int, m int, k int) bool {
	count := 0
	n := len(arr)

	for i := 0; i < n-m; i++ {
		if arr[i] == arr[i+m] {
			count++
		} else {
			count = 0
		}

		if count == m*(k-1) {
			return true
		}
	}

	return false
}
