func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
	const (
		m1 = uint8(0x0F) // . 0000 1111 .
		m2 = uint8(0xF0) // . 1111 0000 .
		m3 = uint8(0x3C) // . 0011 1100 .
	)

	rows := make(map[int]uint8)
	for _, seat := range reservedSeats {
		i, j := seat[0], seat[1]-2
		if j < 0 || j > 7 {
			continue
		}

		rows[i] |= 1 << j
	}

	// optimally an empty row can fit 2 quad seats
	total := (n - len(rows)) * 2

	for _, occ := range rows {
		if m1&occ == 0 || m2&occ == 0 || m3&occ == 0 {
			total++
		}
	}

	return total
}