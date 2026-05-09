func makeFancyString(s string) string {
	if len(s) < 3 {
		return s
	}

	res := []byte(s)
	j := 2

	for i := 2; i < len(res); i++ {
		if res[i] == res[j-1] && res[i] == res[j-2] {
			continue
		}

		res[j] = res[i]
		j++
	}

	res = res[:j]

	return string(res)
}
