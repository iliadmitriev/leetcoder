func minOperations(boxes string) []int {
	N := len(boxes)
	leftCnt, rightCnt := 0, 0
	leftSum, rightSum := 0, 0
	res := make([]int, N)

	for i := 0; i < N; i++ {
		box := int(boxes[i] - '0') // 0 if current box is empty, else 1

		rightCnt += box
		rightSum += (i + 1) * box // abs diff between -1 and i
	}

	for i := 0; i < N; i++ {
		box := int(boxes[i] - '0')

		rightSum -= rightCnt
		rightCnt -= box

		res[i] = leftSum + rightSum

		leftCnt += box
		leftSum += leftCnt

	}

	return res
}
