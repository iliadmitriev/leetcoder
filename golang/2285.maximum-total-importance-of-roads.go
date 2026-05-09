func maximumImportance(n int, roads [][]int) int64 {
	inDegree := make([]int, n)
	for i := 0; i < len(roads); i++ {
		inDegree[roads[i][0]]++
		inDegree[roads[i][1]]++
	}

	sort.Ints(inDegree)
	maxImportance := 0

	for i := 0; i < n; i++ {
		maxImportance += inDegree[i] * (i + 1)
	}

	return int64(maxImportance)
}
