func longestPalindrome(words []string) int {
	cache := make([]int, 26*26)
	total, center := 0, false

	for _, word := range words {
		key := getKeyString(word)
		cache[key]++
	}

	for key, cnt := range cache {
		c1, c2 := getPairChars(key)

		if c1 == c2 {
			total += (cnt / 2) * 4
			if cnt%2 == 1 {
				center = true
			}
		} else {
			cnt2 := cache[getKeyCharsPair(c2, c1)]
			total += min(cnt, cnt2) * 2
		}
	}

	if center {
		total += 2
	}
	return total
}

func getKeyString(word string) int {
	return int(word[0]-'a')*26 + int(word[1]-'a')
}

func getKeyCharsPair(c1, c2 byte) int {
	return int(c1-'a')*26 + int(c2-'a')
}

func getPairChars(key int) (byte, byte) {
	return byte(key/26 + 'a'), byte(key%26 + 'a')
}
