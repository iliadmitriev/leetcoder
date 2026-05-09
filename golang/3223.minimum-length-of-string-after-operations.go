func minimumLength(s string) int {
	freq := make([]int, 26)

	for i := range s {
		freq[s[i]-'a']++
	}

	res := 0
	for _, v := range freq {
		res += 1 + (v-1)%2
	}

	return res
}
