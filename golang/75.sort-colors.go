func sortColors(nums []int) {
	colors := make([]int, 3)

	for _, num := range nums {
		colors[num]++
	}

	for j, i := 0, 0; i < 3; i++ {
		for ; colors[i] > 0; colors[i]-- {
			nums[j] = i
			j++
		}
	}
}
