func findTargetSumWays(nums []int, target int) int {
	cache := make(map[[2]int]int, 0)

	zeros := 0
	numsNoZeros := []int{}

	for _, num := range nums {
		if num == 0 {
			zeros++
		} else {
			numsNoZeros = append(numsNoZeros, num)
		}
	}

	return dfsFindTargetSumWays(0, 0, cache, numsNoZeros, target) * (1 << zeros)
}

func dfsFindTargetSumWays(i, value int, cache map[[2]int]int, nums []int, target int) int {
	if i == len(nums) {
		if value == target {
			return 1
		} else {
			return 0
		}
	}

	if res, ok := cache[[2]int{i, value}]; ok {
		return res
	}

	res := dfsFindTargetSumWays(i+1, value+nums[i], cache, nums, target) + dfsFindTargetSumWays(i+1, value-nums[i], cache, nums, target)
	cache[[2]int{i, value}] = res

	return res
}
