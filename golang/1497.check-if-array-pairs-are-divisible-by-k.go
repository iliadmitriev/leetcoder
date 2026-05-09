func canArrange(arr []int, k int) bool {
	freq := make(map[int]int, k)
	for _, num := range arr {
		freq[(num%k+k)%k]++
	}

	if freq[0]%2 != 0 {
		return false
	}

	if k%2 == 0 && freq[k/2]%2 == 1 {
		return false
	}

	for i := 1; i <= k/2; i++ {
		if freq[i] != freq[k-i] {
			return false
		}
	}

	return true
}
