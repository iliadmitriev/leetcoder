import "sort"

func trimMean(arr []int) float64 {
	sort.Ints(arr)
	n := len(arr)
	k := n * 5 / 100

	total := 0
	for i := k; i < n-k; i++ {
		total += arr[i]
	}

	return float64(total) / float64(n-2*k)
}
