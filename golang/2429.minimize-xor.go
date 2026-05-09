func minimizeXor(num1 int, num2 int) int {
	bits1, bits2 := mPopCount(num1), mPopCount(num2)

	res := num1

	if bits1 > bits2 {
		remove := bits1 - bits2

		for i := 1; remove > 0; i <<= 1 {
			if res&i > 0 {
				res ^= i
				remove--
			}
		}
	} else if bits1 < bits2 {
		add := bits2 - bits1

		for i := 1; add > 0; i <<= 1 {
			if res&i == 0 {
				res |= i
				add--
			}
		}
	}

	return res
}

func mPopCount(num int) int {
	cnt := 0
	for ; num > 0; num &= num - 1 {
		cnt++
	}
	return cnt
}
