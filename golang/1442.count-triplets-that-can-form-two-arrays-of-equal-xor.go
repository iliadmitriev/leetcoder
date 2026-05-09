func countTriplets(arr []int) int {
	n := len(arr)
	count := 0
	var a int

	for i := 0; i < n-1; i++ {
		a = arr[i]
		for j := i + 1; j < n; j++ {
			a ^= arr[j]
			if a == 0 {
				count += j - i
			}
		}
	}

	return count
}
