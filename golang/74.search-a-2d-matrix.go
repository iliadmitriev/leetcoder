func searchMatrix(mat [][]int, target int) bool {
	top, center, bottom := 0, 0, len(mat)
	left, mid, right := 0, 0, len(mat[0])

	for top < bottom {
		center = (top + bottom) / 2
		if mat[center][0] < target {
			top = center + 1
		} else {
			bottom = center
		}
	}

	if top == len(mat) || mat[top][0] > target {
		top -= 1
	}

	if top < 0 {
		return false
	}

	for left < right {
		mid = (left + right) / 2

		if mat[top][mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left < len(mat[0]) && mat[top][left] == target
}