func possibleStringCount(word string) int {
	total := 1
	prev := rune(0)

	for _, ch := range word {
		if ch == prev {
			total++
		}

		prev = ch
	}

	return total
}
