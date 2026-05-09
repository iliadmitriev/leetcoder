func numberAtMostSubarrays(nums []int, k int) int {
	count := 0
	l := 0
	odd := 0

	for r := 0; r < len(nums); r++ {
		odd += nums[r] % 2

		for odd > k {
			odd -= nums[l] % 2
			l++
		}

		count += r - l + 1
	}

	return count
}

func numberOfSubarrays(nums []int, k int) int {
	return numberAtMostSubarrays(nums, k) - numberAtMostSubarrays(nums, k-1)
}
