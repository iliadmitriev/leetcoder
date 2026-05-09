func maximumEnergy(energy []int, k int) int {
	n := len(energy)
	prefix := make([]int, n)

	for i := range n {
		prefix[i] = energy[i]

		if i >= k {
			prefix[i] = max(prefix[i], prefix[i]+prefix[i-k])
		}
	}

	from := max(0, n-k)

	return slices.Max(prefix[from:])
}
