func maxDistance(arrays [][]int) int {
	minItem := arrays[0][0]
	maxItem := arrays[0][len(arrays[0])-1]

	res := 0

	for i := 1; i < len(arrays); i++ {
		res = max(
			res,
			max(
				arrays[i][len(arrays[i])-1]-minItem,
				maxItem-arrays[i][0],
			),
		)

		minItem = min(minItem, arrays[i][0])
		maxItem = max(maxItem, arrays[i][len(arrays[i])-1])
	}

	return res
}
