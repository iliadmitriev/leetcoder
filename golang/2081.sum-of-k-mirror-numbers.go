func mirrorBase10(num int, odd bool) int64 {
	res := num
	x := 0

	if odd {
		x = num
	} else {
		x = num / 10
	}

	for x > 0 {
		res *= 10
		res += x % 10
		x /= 10
	}

	return int64(res)
}

func isPalindromeBaseK(num, k int) bool {
	tmp := make([]int, 0)

	for num > 0 {
		tmp = append(tmp, num%k)
		num /= k
	}

	for i, j := 0, len(tmp)-1; i < j; i, j = i+1, j-1 {
		if tmp[i] != tmp[j] {
			return false
		}
	}

	return true
}

func kMirror(k int, n int) int64 {
	total, count := int64(0), 0
	prev, next := 1, 0

	for count < n {
		next = 10 * prev

		for _, odd := range []bool{false, true} {
			for num := prev; num < next; num++ {
				if count == n {
					return total
				}

				value := mirrorBase10(num, odd)

				if isPalindromeBaseK(int(value), k) {
					total += value
					count++
				}
			}
		}

		prev = next
	}

	return total
}
