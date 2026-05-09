/*


[][][3][5][6][1]

[1,2,3,5,6,1,6] win = 3; diff = 0

*/
func containsNearbyAlmostDuplicate(nums []int, indexDiff int, valueDiff int) bool {
	lo := slices.Min(nums)
	cache := make(map[int]int)

	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}

  // normalize, split to buckets of size 
	kdf := func(x int) int { return (x - lo) / (valueDiff + 1) }

	match := func(key, num int) bool {
		if v, ok := cache[key]; ok && abs(v-num) <= valueDiff {
			return true
		}

		return false
	}

	for i, num := range nums {
		key := kdf(num)

		if match(key, num) || match(key-1, num) || match(key+1, num) {
			return true
		}

		cache[key] = num

		if i-indexDiff >= 0 {
			remove := kdf(nums[i-indexDiff])
			delete(cache, remove)
		}
	}

	return false
}