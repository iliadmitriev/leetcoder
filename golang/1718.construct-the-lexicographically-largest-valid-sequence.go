func constructDistancedSequence(n int) []int {
	m := 2*n - 1
	seq := make([]int, m)
	used := make([]bool, n+1)

	buildSequence(used, seq, 0, n)
	return seq
}

func buildSequence(used []bool, seq []int, idx, n int) bool {
	if idx == len(seq) {
		return true
	}

	if seq[idx] != 0 {
		return buildSequence(used, seq, idx+1, n)
	}

	for num := n; num >= 1; num-- {
		if used[num] {
			continue
		}

		if num == 1 {
			seq[idx] = num
			used[num] = true

			if buildSequence(used, seq, idx+1, n) {
				return true
			}

			used[num] = false
			seq[idx] = 0
		} else {
			if idx+num >= len(seq) || seq[idx+num] != 0 {
				continue
			}

			seq[idx] = num
			seq[idx+num] = num
			used[num] = true

			if buildSequence(used, seq, idx+1, n) {
				return true
			}

			seq[idx] = 0
			seq[idx+num] = 0
			used[num] = false
		}
	}

	return false
}
