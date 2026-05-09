type Positions []int

func (p *Positions) bisectLeft(x int) int {
	arr := *p

	lo, hi := 0, len(arr)
	var mid int
	for lo < hi {
		mid = (lo + hi) / 2

		if arr[mid] < x {
			lo = mid + 1
		} else {
			hi = mid
		}
	}
	return lo
}

func (p *Positions) bisectRight(x int) int {
	arr := *p

	lo, hi := 0, len(arr)
	var mid int

	for lo < hi {
		mid = (lo + hi) / 2

		if arr[mid] > x {
			hi = mid
		} else {
			lo = mid + 1
		}
	}

	return lo
}

func maxTotalFruitsV1(fruits [][]int, startPos int, k int) int {
	n := len(fruits)
	pos := make(Positions, n)
	prefix := make([]int, n+1)

	for i := range n {
		pos[i] = fruits[i][0]
		prefix[i+1] = prefix[i] + fruits[i][1]
	}

	var left, right, start, end, curMax int

	for x := range k/2 + 1 {
		left = startPos - x
		right = startPos + k - 2*x
		start = pos.bisectLeft(left)
		end = pos.bisectRight(right)
		curMax = max(curMax, prefix[end]-prefix[start])

		right = startPos + x
		left = startPos - k + 2*x
		start = pos.bisectLeft(left)
		end = pos.bisectRight(right)
		curMax = max(curMax, prefix[end]-prefix[start])
	}

	return curMax
}

func countSteps(fruits [][]int, startPos, left, right int) int {
	leftPart := startPos - fruits[left][0]
	rightPart := fruits[right][0] - startPos
	both := leftPart + rightPart

	if leftPart <= 0 {
		return rightPart
	} else if rightPart <= 0 {
		return leftPart
	}

	return min(leftPart, rightPart) + both
}

func maxTotalFruitsV2(fruits [][]int, startPos int, k int) int {
	n := len(fruits)
	cur, curMax := 0, 0

	for left, right := 0, 0; right < n; right++ {
		cur += fruits[right][1]

		for left <= right && countSteps(fruits, startPos, left, right) > k {
			cur -= fruits[left][1]
			left++
		}

		curMax = max(curMax, cur)
	}

	return curMax
}

func maxTotalFruits(fruits [][]int, startPos int, k int) int {
	return maxTotalFruitsV2(fruits, startPos, k)
}
