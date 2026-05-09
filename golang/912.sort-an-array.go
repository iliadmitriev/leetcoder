
func sortArray(nums []int) []int {
	return heapSort(nums)
}

func heapSort(arr []int) []int {
	n := len(arr)

	for i := n - 1; i >= 0; i-- {
		heapify(arr, i, n-1)
	}

	for i := n - 1; i > 0; i-- {
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, 0, i-1)
	}

	return arr
}

func heapify(arr []int, start, end int) {
	parent, child := start, 2*start+1

	for child <= end {
		if child < end && arr[child] < arr[child+1] {
			child++
		}

		if arr[parent] < arr[child] {
			arr[parent], arr[child] = arr[child], arr[parent]
			parent, child = child, 2*child+1
		} else {
			break
		}
	}
}
