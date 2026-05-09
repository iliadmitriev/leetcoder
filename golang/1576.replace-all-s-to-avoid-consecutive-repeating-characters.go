
const (
	QUESTION = byte('?')
	SPACE    = byte(' ')
)

func modifyString(s string) string {
	t := []byte(s)
	n := len(t)

	for i, ch := range t {
		if ch != QUESTION {
			continue
		}

		left, right := SPACE, SPACE
		if i > 0 {
			left = t[i-1]
		}
		if i < n-1 {
			right = t[i+1]
		}

		for j := byte('a'); j <= byte('z'); j++ {
			if j != left && j != right {
				t[i] = j
				break
			}
		}
	}

	return string(t)
}
