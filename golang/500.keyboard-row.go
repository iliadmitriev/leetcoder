func findWords(words []string) []string {
	row1 := map[byte]bool{'q': true, 'w': true, 'e': true, 'r': true, 't': true, 'y': true, 'u': true, 'i': true, 'o': true, 'p': true}
	row2 := map[byte]bool{'a': true, 's': true, 'd': true, 'f': true, 'g': true, 'h': true, 'j': true, 'k': true, 'l': true}
	row3 := map[byte]bool{'z': true, 'x': true, 'c': true, 'v': true, 'b': true, 'n': true, 'm': true}

	res := make([]string, 0)
	for _, word := range words {
		candidate := strings.ToLower(word)
		if IsASubset(row1, candidate) || IsASubset(row2, candidate) || IsASubset(row3, candidate) {
			res = append(res, word)
		}
	}

	return res
}

func IsASubset(superSet map[byte]bool, subSet string) bool {
	for i := range subSet {
		if _, ok := superSet[subSet[i]]; !ok {
			return false
		}
	}

	return true
}
