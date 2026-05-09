func maxDistance(s string, k int) int {
	longest := 0
	lat, lon := 0, 0

	abs := func(i int) int {
		if i < 0 {
			return -i
		}
		return i
	}

	for i, d := range s {
		switch d {
		case 'N':
			lat++
		case 'S':
			lat--
		case 'E':
			lon++
		case 'W':
			lon--
		}

		longest = max(longest, min(abs(lat)+abs(lon)+2*k, i+1))

	}

	return longest
}
