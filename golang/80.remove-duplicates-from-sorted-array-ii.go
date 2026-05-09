//                k
// [0,0,1,1,2,3,3,3,3]
// c = 2
func removeDuplicates(nums []int) int {
	n := len(nums)
	prev := -1
	k := 0
	c := 0

	for i := 0; i < n; i++ {
		if prev != nums[i] { // not duplicate
			nums[k] = nums[i]
      prev = nums[k]
			k++
			c = 1
		} else if c < 2 { // first or second duplicate
			nums[k] = nums[i]
      prev = nums[k]
			k++
			c++
    } // otherwise c >= 2: do nothing
	}

	return k
}