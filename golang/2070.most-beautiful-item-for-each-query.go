func maximumBeauty(items [][]int, queries []int) []int {
	m, n := len(items), len(queries)

	sort.Slice(items, func(i, j int) bool {
		if items[i][0] < items[j][0] {
			return true
		} else {
			return items[i][0] == items[j][0] && items[i][1] < items[j][1]
		}
	})

	data := make([][2]int, 0, m)
	maxBeaty := 0
	for i := 0; i < m; i++ {
		maxBeaty = max(maxBeaty, items[i][1])
		data = append(data, [2]int{items[i][0], maxBeaty})
	}

	result := make([]int, n)
	var k int
	for j := 0; j < n; j++ {
		k = binSearchPair(data, queries[j])

		if k > 0 {
			k--
			result[j] = data[k][1]
		}
	}

	return result
}

func binSearchPair(data [][2]int, target int) int {
	lo, hi := 0, len(data)
	var mid int
	for lo < hi {
		mid = (lo + hi) / 2

		if data[mid][0] > target {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}
