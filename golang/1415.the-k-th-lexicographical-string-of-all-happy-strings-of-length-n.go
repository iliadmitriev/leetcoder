func getHappyString(n int, k int) string {
	count := 0

	var bt func(byte, []byte) string

	bt = func(prev byte, cur []byte) string {
		if n == len(cur) {
			count++

			if count == k {
				return string(cur)
			}

			return ""
		}

		for ch := byte('a'); ch <= 'c'; ch++ {
			if prev == ch {
				continue
			}

			res := bt(ch, append(cur, ch))

			if len(res) > 0 {
				return res
			}
		}

		return ""
	}

	return bt('#', []byte{})
}