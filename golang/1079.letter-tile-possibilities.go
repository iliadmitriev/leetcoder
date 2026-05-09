func numTilePossibilities(tiles string) int {
	chars := make([]int, 26)
	for _, c := range []byte(tiles) {
		chars[c-'A']++
	}

	return backTrackNumTiles(tiles, chars)
}

func backTrackNumTiles(tiles string, chars []int) int {
	total := 0

	for i := 0; i < 26; i++ {
		if chars[i] == 0 {
			continue
		}

		total += 1
		chars[i]--
		total += backTrackNumTiles(tiles, chars)
		chars[i]++

	}

	return total
}
