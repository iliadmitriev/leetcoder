func smallestNumber(n int) int {
	bits := bits.Len(uint(n))
	return (1 << bits) - 1
}
