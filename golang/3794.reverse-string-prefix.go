func reversePrefix(s string, k int) string {
	k = min(k, len(s))
	buf := []byte(s[:k])

	for i, j := 0, k-1; i < j; i, j = i+1, j-1 {
    buf[i], buf[j] = buf[j], buf[i]
	}

  return string(buf) + s[k:]
}