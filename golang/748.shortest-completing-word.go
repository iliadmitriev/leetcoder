import "strings"

func shortestCompletingWord(licensePlate string, words []string) string {
	plate := _charCountKey(licensePlate)
	minLen := 1000
	result := ""

	for _, w := range words {
		if _compareCharCount(plate, _charCountKey(w)) && minLen > len(w) {
			minLen = len(w)
			result = w
		}
	}

	return result
}

func _compareCharCount(key1, key2 []int) bool {
	if len(key1) != len(key2) {
		return false
	}

	for i := 0; i < len(key1); i++ {
		if key1[i] > key2[i] {
			return false
		}
	}

	return true
}

func _charCountKey(key string) []int {

	w := strings.ToLower(key)
	cCount := make([]int, 26)

	for i := 0; i < len(w); i++ {
		if 'a' <= w[i] && w[i] <= 'z' {
			c := w[i] - 'a'
			cCount[c]++
		}
	}

	return cCount
}
