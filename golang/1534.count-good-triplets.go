func countGoodTriplets(arr []int, a int, b int, c int) int {
	count := 0
	n := len(arr)

	for j := n - 2; j >= 0; j-- {
		arr_b := make([]int, 0, n-j)
		for k := j + 1; k < n; k++ {
			diff := arr[j] - arr[k]
			if abs(diff) <= b {
				insortRight(&arr_b, diff)
			}
		}

		for i := 0; i < j; i++ {
			diff := arr[i] - arr[j]
			if abs(diff) <= a {
				lower := bisectLeft(arr_b, -c-diff)
				upper := bisectRight(arr_b, c-diff)
				count += upper - lower
			}
		}
	}

	return count
}

func abs(x int) int {
	if x < 0 {
		return -x
	}

	return x
}

func bisectLeft(arr []int, x int) int {
	l := 0
	r := len(arr)
	var m int
	for l < r {
		m = (l + r) / 2

		if arr[m] < x {
			l = m + 1
		} else {
			r = m
		}
	}

	return l
}

func bisectRight(arr []int, x int) int {
	l := 0
	r := len(arr)
	var m int
	for l < r {
		m = (l + r) / 2

		if x < arr[m] {
			r = m
		} else {
			l = m + 1
		}
	}

	return l
}

func insortRight(arr *[]int, x int) {
	i := bisectRight(*arr, x)
	*arr = append((*arr)[:i+1], (*arr)[i:]...)
	(*arr)[i] = x
}
