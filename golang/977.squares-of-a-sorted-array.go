func sortedSquares(nums []int) []int {
	i, j := 0, len(nums)-1
	res := make([]int, len(nums))
  k := len(nums) - 1

	for i <= j {
    a, b := nums[i], nums[j]

    a *= a
    b *= b

    if a > b {
      res[k] = a
      i++
    } else {
      res[k] = b
      j--
    }

    k--
	}

  return res
}