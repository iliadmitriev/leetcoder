package main

func minBitFlips(start int, goal int) int {
	start ^= goal
	n := 0

	for start > 0 {
		n++
		start &= start - 1
	}

	return n
}
