const MMOD = int(1e9) + 7

func numOfSubarrays(arr []int) int {
	odd, even, total := 0, 0, 0
	for _, num := range arr {
		total += num
		if total%2 == 0 {
			even++
		} else {
			odd++
		}
	}

	return odd * (1 + even) % MMOD
}
