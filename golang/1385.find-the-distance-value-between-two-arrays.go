func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	w := d + 1
	bucket := func(x int) int {
		// fix Intels floor division for negatives
		if x < 0 {
			return (x+1)/w - 1
		}
		return x / w
	}

	lo := map[int]int{} // buckets with lowest values
	hi := map[int]int{} // buckets with highest values

	for _, b := range arr2 {
		k := bucket(b)

		if m, ok := lo[k]; !ok || b < m {
			lo[k] = b
		}

		if m, ok := hi[k]; !ok || b > m {
			hi[k] = b
		}
	}

	count := 0

	for _, a := range arr1 {
		k := bucket(a)
		_, own := lo[k]
		left, hasLeft := hi[k-1]   // highest value from the left
		right, hasRight := lo[k+1] // lowest value from the right

		if !own && (!hasLeft || left < a-d) && (!hasRight || a+d < right) {
			count++
		}
	}

	return count
}