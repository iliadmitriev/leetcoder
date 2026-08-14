func maximumLengthSubstring(s string) int {
	const (
		k    = 2
		base = byte('a')
	)

	win := [26]int{}
	largest := 0
	n := len(s)

	for i, j := 0, 0; i < n; i++ {
		win[s[i]-base]++

		for win[s[i]-base] > k {
			win[s[j]-base]--
			j++
		}

		largest = max(largest, i-j+1)
	}

	return largest
}