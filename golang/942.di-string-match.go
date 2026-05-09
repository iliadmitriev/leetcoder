
func diStringMatch(s string) []int {
	result := make([]int, len(s)+1)
	lo, hi := 0, len(s)

	for i := 0; i < len(s); i++ {
		if s[i] == 'I' {
			result[i] = lo
			lo++
		} else {
			result[i] = hi
			hi--
		}
	}

	result[len(s)] = lo
	return result
}
