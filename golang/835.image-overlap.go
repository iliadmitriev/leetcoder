func largestOverlap(img1 [][]int, img2 [][]int) int {
	n := uint32(len(img1))

	// we store coordinates packed in uint32 type
	// key is (row << shift) | col
  // values range in [0; 60]
  // we need min 6 bits to store values up to 64
	const shift = 6               // row shift
	const mask = (1 << shift) - 1 // column mask

	ones1 := make([]uint32, 0)
	ones2 := make([]uint32, 0)

	for i := uint32(0); i < n; i++ {
		for j := uint32(0); j < n; j++ {
			if img1[i][j] == 1 {
				ones1 = append(ones1, (i<<shift)|j)
			}

			if img2[i][j] == 1 {
				ones2 = append(ones2, (i<<shift)|j)
			}
		}
	}

	// map: coordinate diff -> count
	freq := make(map[uint32]int)

	// calculate all the points cross coordinate differencies
	// and collect their counts
	for _, rc1 := range ones1 {
		for _, rc2 := range ones2 {
			r1, c1 := rc1>>shift, rc1&mask
			r2, c2 := rc2>>shift, rc2&mask

			key := ((n + r2 - r1) << shift) | (n + c2 - c1)
			freq[key]++
		}
	}

	max_count := 0
	for _, count := range freq {
		max_count = max(max_count, count)
	}
	return max_count
}