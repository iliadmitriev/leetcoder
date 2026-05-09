func minimumPushes(word string) int {
	const (
		N    = 26
		KEYS = 8
	)

	freq := make([]int, N)
	for i := 0; i < len(word); i++ {
		freq[word[i]-'a']++
	}

	sort.Slice(freq, func(i, j int) bool {
		return freq[i] > freq[j]
	})

	res := 0
	for i := 0; i < N; i++ {
		res += (i/KEYS + 1) * freq[i]
	}

	return res
}
