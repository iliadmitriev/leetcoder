func findLengthOfShortestSubarray(arr []int) int {
	n := len(arr)
	i, j := 0, n-1

	for i < j && arr[i] <= arr[i+1] {
		i++
	}

	if i == n-1 {
		return 0
	}

	minLen := n - i - 1

	for i < j && arr[j-1] <= arr[j] {
		j--
	}

	minLen = min(minLen, j)

	left := i
	i = 0

	for i <= left && j < n {
		if arr[i] <= arr[j] {
			minLen = min(minLen, j-i-1)
			i++
		} else {
			j++
		}
	}

	return minLen
}
