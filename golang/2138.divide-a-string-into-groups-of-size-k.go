func divideString(s string, k int, fill byte) []string {
	res := make([]string, 0, len(s)/k+1)
	for i := 0; i < len(s); i += k {
		res = append(res, s[i:min(i+k, len(s))])
	}

	for len(res[len(res)-1]) < k {
		res[len(res)-1] += string(fill)
	}

	return res
}
