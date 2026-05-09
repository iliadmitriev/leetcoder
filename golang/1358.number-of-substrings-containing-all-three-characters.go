func numberOfSubstrings(s string) int {
	N := len(s)
	count := 0
	left := 0
	win := make([]int, 3)

	for right := 0; right < N; right++ {
		win[s[right]-'a']++
		for win[0] > 0 && win[1] > 0 && win[2] > 0 {
			count += N - right
			win[s[left]-'a']--
			left++
		}
	}

	return count
}
