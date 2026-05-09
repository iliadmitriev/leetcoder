func smallestRangeI(nums []int, k int) int {
	_min, _max := _minArr(nums)+k, _maxArr(nums)-k
	return max(0, _max-_min)
}

func _maxArr(arr []int) int {
	m := arr[0]
	for i := range arr {
		if arr[i] > m {
			m = arr[i]
		}
	}

	return m
}

func _minArr(arr []int) int {
	m := arr[0]
	for i := range arr {
		if arr[i] < m {
			m = arr[i]
		}
	}

	return m
}