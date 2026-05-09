func flipAndInvertImage(image [][]int) [][]int {
	m, n := len(image), len(image[0])

	for i := 0; i < m; i++ {
		for j := 0; j < n/2; j++ {
			image[i][j], image[i][n-1-j] = image[i][n-1-j], image[i][j]
		}
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			image[i][j] = 1 - image[i][j]
		}
	}

	return image
}
