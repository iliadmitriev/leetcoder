func totalFruit(fruits []int) int {
	maxFruits := 0
	bothCnt, oneCnt := 0, 0 // current and prev counter, current counter
	A, B := -1, -1

	for _, f := range fruits {
		if f == A || f == B {
			bothCnt++
		} else {
			bothCnt = oneCnt + 1
		}

		if f == A {
			oneCnt++
		} else {
			B = A
			A = f
			oneCnt = 1
		}

		maxFruits = max(maxFruits, bothCnt)
	}

	return maxFruits
}
