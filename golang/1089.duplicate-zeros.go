func duplicateZeros(arr []int) {
	n := len(arr)

	z := 0 // number of zeroes to the left of pointer i
	for _, v := range arr {
		if v == 0 {
			z++
		}
	}

	for i := n - 1; i >= 0 && z > 0; i-- {
		if i+z < n {
			arr[i+z] = arr[i]
		}

		if arr[i] == 0 {
			z--

			if i+z < n {
				arr[i+z] = 0
			}
		}
	}

}
