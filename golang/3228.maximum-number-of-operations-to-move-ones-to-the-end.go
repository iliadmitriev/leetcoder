
func maxOperations(s string) int {
	inc := 0
	cnt := 0

	pre := byte('1')

	for i := len(s) - 1; i >= 0; i-- {
		if pre != '0' && s[i] == '0' {
			inc++
		} else if s[i] == '1' {
			cnt += inc
		}

		pre = s[i]
	}

	return cnt
}
