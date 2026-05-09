func canBeEqual(target []int, arr []int) bool {
	if len(target) != len(arr) {
		return false
	}

	mp := make(map[int]int, len(target))

	for _, v := range arr {
		mp[v]++
	}

	for _, v := range target {
		if mp[v] == 0 {
			return false
		}
		mp[v]--
	}

	return true
}
