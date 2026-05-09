func decode(encoded []int, first int) []int {
	n := len(encoded)
	decoded := make([]int, 0, n)

	decoded = append(decoded, first)

	for i := 0; i < n; i++ {
		decoded = append(decoded, encoded[i]^decoded[i])
	}

	return decoded
}
