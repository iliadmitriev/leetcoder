func threeConsecutiveOdds(arr []int) bool {
	n := len(arr)

	for i := range n - 2 {
		if arr[i]%2 == 1 && arr[i+1]%2 == 1 && arr[i+2]%2 == 1 {
			return true
		}
	}

	return false
}
