func restoreString(s string, indices []int) string {
	res := make([]byte, len(s))

	for i := range s {
		res[indices[i]] = s[i]
	}

	return string(res)
}
