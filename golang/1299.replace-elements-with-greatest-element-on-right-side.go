func replaceElements(arr []int) []int {
	maxRight := -1

	for i := len(arr) - 1; i >= 0; i-- {
		arr[i], maxRight = maxRight, max(arr[i], maxRight)
	}

	return arr
}
