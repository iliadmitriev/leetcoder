package main

func wonderfulSubstrings(word string) int64 {
	res, mask := 0, 0

	freq := make([]int, 1024)
	freq[0] = 1

	for i := 0; i < len(word); i++ {
		mask ^= 1 << (word[i] - 'a')
		freq[mask]++
	}

	for mask := 0; mask < 1024; mask++ {
		if freq[mask] == 0 {
			continue
		}

		res += freq[mask] * (freq[mask] - 1) / 2
		for i := 0; i < 10; i++ {
			mask2 := mask ^ (1 << i)
			if mask2 < mask {
				res += freq[mask] * freq[mask2]
			}
		}
	}

	return int64(res)
}
