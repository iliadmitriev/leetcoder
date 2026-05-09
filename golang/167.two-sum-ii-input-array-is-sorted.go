func twoSum(nums []int, target int) []int {

  binsearch := func(arr []int, lo, x int) int {
    hi := len(arr)
    for lo < hi {
      mid := (lo + hi) / 2
      if arr[mid] < x {
        lo = mid + 1
      } else {
        hi = mid
      }
    }

    return lo
  }

	n := len(nums)
	for i, num1 := range nums {
    j := binsearch(nums, i + 1, target - num1)

		if j < n && nums[j]+num1 == target {
			return []int{i + 1, j + 1}
		}
	}

	return []int{}
}