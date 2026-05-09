func threeSum(nums []int) [][]int {
	res := make([][]int, 0)
	sort.Ints(nums)
	n := len(nums)

	comb := func(i int) {
		target := nums[i]
		left := i + 1
		right := n - 1

		for left < right {
			s := nums[left] + nums[right]

			if target == -s {
				res = append(res, []int{target, nums[left], nums[right]})
			}

			if target < -s {
				prev := nums[left]
				for left < right && prev == nums[left] {
					left++
				}
			} else {
				prev := nums[right]
				for left < right && prev == nums[right] {
					right--
				}

			}
		}
	}

	for i := range n {
    if i > 0 && nums[i - 1] == nums[i] {
      continue
    }

    if nums[i] > 0 {
      break
    }

		comb(i)
	}

	return res
}
