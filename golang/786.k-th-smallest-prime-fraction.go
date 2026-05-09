
// countLessThan returns the number of fractions smaller than val.
// Those fractions built from two numbers from the array
func countLessThan(arr []int, val float64) (int, int, int) {
	count := 0
	n := len(arr)
	p, q := 0, n-1
	maxFrac := float64(arr[p]) / float64(arr[q])

	j := 1
	for i := 0; i < n-1; i++ {
		for j < n && float64(arr[i])/float64(arr[j]) > val {
			j++
		}

		if j == n {
			break
		}

		if maxFrac < float64(arr[i])/float64(arr[j]) {
			maxFrac = float64(arr[i]) / float64(arr[j])
			p, q = i, j
		}

		count += (n - j)
	}

	return count, p, q
}

func kthSmallestPrimeFraction(arr []int, k int) []int {
	n := len(arr)
	low, high := 0.0, 1.0
	var mid float64
	var cnt, num, denom int

	for low < high {
		mid = (high + low) / 2.0
		cnt, num, denom = countLessThan(arr, mid)

		if cnt == k {
			return []int{arr[num], arr[denom]}
		} else if cnt < k {
			low = mid
		} else {
			high = mid
		}
	}

	return []int{arr[0], arr[n-1]}
}
